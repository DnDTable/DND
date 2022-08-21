import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
// import App from './App';
import reportWebVitals from './reportWebVitals';
// import GameTableMap from './GameTableMap';
import GameTableBoss from './GameTableBoss';

var table;
// table = <GameTableMap />;
table = <GameTableBoss />;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
        {/* <div><input class="" type="checkbox" id="switch_map_cheakbox"></input></div> */}
        <div class="conteiner">
            <div class="game_table">
                {table}
            </div>
            <div class="side_panel">
                <p>Players:</p>
                <div class="players_list">
                    <div class="player_card">
                        <div class="portret"></div>
                        <p>Player</p>
                    </div>
                    <div class="player_card">
                    <div class="portret portret_2"></div>
                        <p>Player</p>
                    </div>
                    <div class="player_card">
                    <div class="portret portret_3"></div>
                        <p>Player</p>
                    </div>
                    <div class="player_card">
                    <div class="portret portret_4"></div>
                        <p>Player</p>
                    </div>
                </div>
                <p>Active spells:</p>
                {/* <div class="players_list">
                    <button onClick="">click me</button>
                </div> */}
            </div>
        </div>
    </React.StrictMode>
);
reportWebVitals();
