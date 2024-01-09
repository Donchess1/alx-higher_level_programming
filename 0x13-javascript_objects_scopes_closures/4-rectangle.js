class Rectangle{
    constructor(w, h) {
        if ((w > 0) && (h > 0)){
            this.width = w;
            this.height = h;
        }
    }
    print() {
        for (let a = 0; a < this.height; a++){
            let b = "X".repeat(this.width);
            console.log(b);
        }
    }
    rotate() {
        let a = this.width;
        this.width = this.height;
        this.height = a;
    }
    double() {
        this.width *= 2;
        this.height *= 2;
    }
}
module.exports = Rectangle;