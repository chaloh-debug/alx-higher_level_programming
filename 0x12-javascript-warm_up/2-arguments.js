#!/usr/bin/node
if (process.args.length < 3) {
    console.log('No argument');
} else if (process.args.length === 3) {
    console.log('Argument found');
}
else {
    console.log('Arguments found');
}
