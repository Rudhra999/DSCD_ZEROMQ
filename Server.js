const zmq = require("zeromq");
const sock = new zmq.Push();
run();
async function run(){
    await sock.bind("tcp://127.0.0.1:7000");
    console.log("Server is Listening on port 7000");
    process.stdin.once("data",send);
}

async function send(){
    console.log("About to send Jobs !");
    for(let i=0;i<100;i++){
        await sock.send('Sendind Jobs ${i}');

        await new Promise(resolve=>setTimeout(resolve,500));
    }
}