import React, {useState} from 'react';
import './GameTableMap.css';

function GameTableMap() {
    // console.warn("asdasdasdasdasdasdasdasdads: " + App.)
    const [cellTemp, setCellTemp] = useState(
    )


    const[cells, setCells] = useState ([
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
        {id: 0, text: "none"},
    ])


    const[currentPlayerColor, setCurrentPlayerColor] = useState("#0075ff")

    function dragStartHeandler (e, card){
        console.log('drag', card)
    }

    function dragLeaveHeandler(e){
        e.target.style.background = {currentPlayerColor}
    }

    function dragEndHeandler(e){
        e.target.style.background = {currentPlayerColor}
    }

    function dragOverHeandler(e){
        // if (e.target.className == "cell")
        //     console.log( card.className)
        // if(true){ // e.className == "cell"
        //     e.preventDefault()
        //     // e.target.style.background = 'lightgray'
        // }
        e.preventDefault()
    }
    
    function DropHeandler(e, card){
        e.preventDefault()
        // console.log('drop')
        // console.log('drop is', card)
        // console.log('drop to', e)
        e.target.text = 'yes it'
        e.target.style.background = 'red';
        // e.style.background = 'green';
    }
    
    return (
        <div className="game_table_map" >
            <table>
                {cells.map((cell) =>
                    <div className="cells"
                    draggable = {false}
                    onDragStart = {(e) => dragStartHeandler(e, this)}
                    onDragLeave = {(e) => dragLeaveHeandler(e)}
                    onDragEnd = {(e) => dragEndHeandler(e)}
                    onDragOver = {(e) => dragOverHeandler(e)}
                    onDrop = {(e) => DropHeandler(e, this)}>
                        {/* <p>{cell.text}</p> */}
                    </div>
                )}
                {/* {playerCards.map((card) =>
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
                    )} */}
            </table>
        </div>
    );
}

export default GameTableMap;

{/* <tr>
<th className="cell"
    draggable = {false}
    onDragStart = {(e) => dragStartHeandler(e, this)}
    onDragLeave = {(e) => dragLeaveHeandler(e)}
    onDragEnd = {(e) => dragEndHeandler(e)}
    onDragOver = {(e) => dragOverHeandler(e)}
    onDrop = {(e) => DropHeandler(e, this)}>
    asd
</th>
<th className="cell"
draggable = {false}
onDragStart = {(e) => dragStartHeandler(e, this)}
onDragLeave = {(e) => dragLeaveHeandler(e)}
onDragEnd = {(e) => dragEndHeandler(e)}
onDragOver = {(e) => dragOverHeandler(e)}
onDrop = {(e) => DropHeandler(e, this)}>asd</th>
<th className="cell">asd</th>
</tr>
<tr>
<th className="cell">dsa</th>
<th className="cell">dsa</th>
<th className="cell">dsa</th>
</tr>
<tr>
<th className="cell">qwe</th>
<th className="cell">qwe</th>
<th className="cell">qwe</th>
</tr> */}
// const[cardList, setCardList] = useState([
//     {id:1, order:3, text: 'КАРТОЧКА 3'},
//     {id:2, order:4, text: 'КАРТОЧКА 4'},
//     {id:3, order:2, text: 'КАРТОЧКА 2'},
//     {id:4, order:1, text: 'КАРТОЧКА 1'}
// ])

// const[currntCard, setCurrentCard] = useState(null)

// function dragStartHeandler (e, card){
//     console.log('drag', card)
//     setCurrentCard(card)
// }

// function dragLeaveHeandler(e){
//     e.target.style.background = 'white'
// }

// function dragEndHeandler(e){
//     e.target.style.background = 'white'
// }

// function dragOverHeandler(e){
//     e.preventDefault()
//     e.target.style.background = 'lightgray'
// }

// function DropHeandler(e, card){
//     e.preventDefault()
//     console.log('drop', card)
//     setCardList(cardList.map(c => {
//         if (c.id === card.id){
//             return {...c, order: currntCard.order}
//         }
//         if (c.id === currntCard.id){
//             return {...c, order: card.order}
//         }
//         return c
//     }))
//     e.target.style.background = 'white'
// }

// const sortCard = (a, b) => {
//     if (a.order > b.order){
//         return 1
//     }
//     else{
//         return -1
//     }
// }

// return (
//     <div classNameName="App">
//         {cardList.sort(sortCard).map(card => 
//             <div 
//                 classNameName={'card'}
//                 draggable = {true}
//                 onDragStart = {(e) => dragStartHeandler(e, card)}
//                 onDragLeave = {(e) => dragLeaveHeandler(e)}
//                 onDragEnd = {(e) => dragEndHeandler(e)}
//                 onDragOver = {(e) => dragOverHeandler(e)}
//                 onDrop = {(e) => DropHeandler(e, card)}
//                 >
                
//                 {card.text}
//             </div>
//         )}
//     </div>
// );