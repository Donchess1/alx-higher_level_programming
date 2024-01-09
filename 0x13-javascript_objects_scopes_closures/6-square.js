#!/usr/bin / node
const SquareP = require('./5-square');

class Square extends SquareP {
    charPrint (c) {
        if (c === undefined) {
            c = "X";
        }
        for (let a = 0; a < this.width; a++){
            let b = c.repeat(this.height);
            console.log(b);
        }
    }
}
module.exports = Square;