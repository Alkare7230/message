



let http = require('http')
let fs = require('fs')


let server = http.createServer((request, response) => { 
    
    
    fs.readFile('index.html', (err, data) => {
if (err) {
    response.writeHead(404)
    response.end('Not Found')

} else{
    response.writeHead(200, {

        'content-type':'text/html; charset=utf-8'
    })
    response.end(data)
}


})


}).listen(8070)