const ping = require('ping');

function pingHost(targetIp) {
  const host = ping.sys.probe(targetIp, function(isAlive) {
    const msg = isAlive ? 'host ' + targetIp + ' is alive' : 'host ' + targetIp + ' is dead';
    console.log(msg);
  });
}

// Example usage:
pingHost('8.8.8.8');