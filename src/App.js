import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import GameTableMap from './GameTableMap';
import GameTableBoss from './GameTableBoss';


const tables = [<GameTableMap/>, <GameTableBoss/>]
function App() {  
    const[currentTable, setCurrentTable] = useState(<GameTableMap/>)
    const[playerCards, setPlayersCards] = useState([
        {id: 0, order: 0, name: "Player 0", className: "player_card", portret: "portret" },
        {id: 1, order: 1, name: "Player 1", className: "player_card", portret: "portret portret_2" },
        {id: 2, order: 2, name: "Player 2", className: "player_card", portret: "portret portret_3" },
        {id: 3, order: 3, name: "Player 3", className: "player_card", portret: "portret portret_4" },
    ])
    const[currentPlayerCard, setCurrentPlayersCard] = useState()
    const[currentPlayerColor, setCurrentPlayerColor] = useState("#0075ff")

    function ChangeTable(e){
        if (currentTable == tables[1]){
            e.preventDefault();
            setCurrentTable(tables[0])
        }
        else{
            e.preventDefault();
            setCurrentTable(tables[1])
        }
    }

    function dragStartHeandler (e, card){
        // console.log('drag', card)
        setCurrentPlayersCard(card)
    }

    function dragLeaveHeandler(e){
        e.target.style.background = {currentPlayerColor}
    }

    function dragEndHeandler(e){
        e.target.style.background = {currentPlayerColor}
    }

    function dragOverHeandler(e){
        if (e.target.className == "cell")
            console.log(e.target.className)
        if(true){ // e.className == "cell"
            e.preventDefault()
            // e.target.style.background = 'lightgray'
        }
    }

    function DropHeandler(e, card){
        e.preventDefault()
        console.log('drop')
        console.log('drop iss', card)
        console.log('drop to', e)

        // setPlayersCards(playerCards.map(c => {
        //     if (c.id === card.id){
        //         return {...c, order: currentPlayerCard.order}
        //     }
        //     if (c.id === currentPlayerCard.id){
        //         return {...c, order: card.order}
        //     }
        //     return c
        // }))
        // e.target.style.background = {currentPlayerColor}
    }

    const sortCard = (a, b) => {
        if (a.order > b.order){
            return 1
        }
        else{
            return -1
        }
    }


    return (
        <div className="conteiner">
            <div className="game_table">
                {currentTable}
            </div>
            <div className="side_panel">
                <button className="side_button" onClick={ChangeTable}>Change Table</button>
                <p>Players:</p>
                <div className="players_list">
                    {playerCards.sort(sortCard).map((card) =>
                        <div className={card.className}
                        draggable = {true}
                        onDragStart = {(e) => dragStartHeandler(e, card)}
                        onDragLeave = {(e) => dragLeaveHeandler(e)}
                        onDragEnd = {(e) => dragEndHeandler(e)}
                        onDragOver = {(e) => dragOverHeandler(e)}
                        onDrop = {(e) => DropHeandler(e, card)}>

                            <div className={card.portret}></div>
                            <p>{card.name}</p>
                        </div>
                    )}
                </div>
                <p>Active spells:</p>
                <div className="players_list">
                    <button className="side_button" onClick="">click me</button>
                </div>
            </div>
        </div>
    );
}

export default App;
