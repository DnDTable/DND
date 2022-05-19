
export const plusSlides = (n)=>{
    
    const canvas = document.getElementById('game_table');
    alert(canvas.width);
    const ctx = canvas.getContext('2d');
    

    const a = 2 * Math.PI / 6;
    const r = 50;
    
    // drawGrid(canvas.width, canvas.height, ctx);
    // function drawGrid(width, height, draw_el) {
    //     alert(n);
    //     for (let y = r; y + r * Math.sin(a) < height; y += r * Math.sin(a)) {
    //         for (let x = r, j = 0; x + r * (1 + Math.cos(a)) < width; x += r * (1 + Math.cos(a)), y += (-1) ** j++ * r * Math.sin(a)) {
    //             drawHexagon(x, y, draw_el);
    //         }
    //     }
    // }
    // function drawHexagon(x, y, draw_el) {
    //     draw_el.beginPath();
    //     for (let i = 0; i < 6; i++) {
    //         draw_el.lineTo(x + r * Math.cos(a * i), y + r * Math.sin(a * i));
    //     }
    //     draw_el.closePath();
    //     draw_el.stroke();
    // }
}



