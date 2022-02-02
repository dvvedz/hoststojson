const process = require('process');
const stream = require('stream');

function hostsToJson() {
    let userInput = process.argv[2]
    let data
    let hostsObject = {}

    if (!userInput == undefined || !userInput == "") {
        const fs = require('fs')

        try {
            data = fs.readFileSync(userInput, 'utf8')

            let lines = data.split("\n");

            lines.forEach((ele) => {
                if(!ele.includes("#")) {
                    let line = ele.split(" ")

                    if (!ele === "" || ele.length > 1) {
                        line.forEach((el) => {
                            if(el.length > 1) {

                                line.shift()

                                line.forEach((domain) => {
                                    if (!domain == "" || domain.length > 1) {
                                        if(domain != "localhost") {
                                            // I have to recreate the array here cuz I used the shift() function - this is cuz i need the ip back in this loop
                                            line = ele.split(" ")
                                            ip = line[0]
                                            hostsObject[`${domain.toString()}`] = ip;
                                        }
                                    }
                                })
                            }
                        })
                    }
                }
            })
            return hostsObject
        } catch (err) {
            console.error(err)
        }
    } else {
        console.error("Error: ", userInput)
    }
}


console.log(JSON.parse(JSON.stringify(hostsToJson())))