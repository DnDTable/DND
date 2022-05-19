import React from 'react';

var cube_1 = 0;
var cube_2 = 0;

function GameTableBoss() {
    function getRandomArbitrary(min, max) {
        return  Math.floor(Math.random() * (max - min) + min);
    }
    function dice(){
        cube_1 = getRandomArbitrary(0, 20);
        cube_2 = getRandomArbitrary(0, 20);
    }
    return (
        <div class="game_table_boss" >
            <div class="game_table_boss_div first"></div>
            <div class="game_table_boss_div second">
                <p>Первый куб: {cube_1}, второй куб: {cube_2}, сумма: {cube_1 + cube_2}</p>
                <div class="rolle_btn" onClick={dice()}><button ><img src='/dice.png' width="60" height="60"></img></button></div>
            </div>
            <div class="game_table_boss_div third"></div>
        </div>
    );
}

export default GameTableBoss;
