var express = require('express');

// instance //

var server = express();
server.get('/', (request, response) => {

    response.setHeader('content-type', 'text/html');
    response.status(200).send('index.html')

});
server.listen(8050, (response, require) => {
console.log("Lancement du programme...")


});
