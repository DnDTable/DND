import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import {plusSlides} from './grid'


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
            <App />
            <div class="conteiner">
                <div class="game_table">
                    <canvas class="game_table_map" >
                    
                    </canvas>
                    <div class="game_table_location">
                        <div class="table_boss">
                            
                        </div>
                        <div class="table_cubes">
                            
                        </div>
                        <div class="table_players">
                            
                        </div>
                    </div>
                </div>
                <div class="side_panel">
                    <div class="players_list">
                        <div class="player_card">
                            <p>Player</p>
                        </div>
                        <div class="player_card">
                            <p>Player</p>
                        </div>
                        <div class="player_card">
                            <p>Player</p>
                        </div>
                        <div class="player_card">
                            <p>Player</p>
                        </div>
                    </div>
                    <div class="players_list">

                    </div>
                </div>
            </div>
    </React.StrictMode>
);
reportWebVitals();
