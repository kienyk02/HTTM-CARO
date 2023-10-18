import React, {useState } from 'react';
import "./assets/css/style.css"
import { Link,useParams } from 'react-router-dom';
import imgwin from "./assets/img/imgwin.png"
import imglose from "./assets/img/imglose.png"
function Playing() {
    const rows = 20;
    const cols = 20;
    const [user,setUser]=useState({
        id:1,
        username:"sa",
        password:"123",
        highScore:"8"
    })
    const level=useParams().level
    const [boardgame,setBoardgame] =useState(Array.from({ length: rows }, () =>Array.from({ length: cols }, () => 0)))
    const [gameActive,setGameActive]=useState(true)
    const [startTime,setStartTime]=useState(null)
    const [imgend,setImgend]=useState(imgwin)
    const [currentPlay,setCurrentPlay]=useState(1)

    function cellClicked(event,row,col) {
        if(startTime==null){setStartTime(performance.now())}
        const cell = event.target;
        if(gameActive && currentPlay==1 && cell.innerText==""){
            setCurrentPlay(0)
            cell.innerHTML = "X";
            cell.className = "cell x";
            let boardtemp=[...boardgame]
            boardtemp[row][col]=1
            if(finalState(boardtemp)){
                setGameActive(false)
                console.log("You win!")
                saveMatchResult(true)
            }else{
                aiMove(boardtemp)
            }
        }
    }

    function aiMove(boardtemp){
        fetch(`http://127.0.0.1:5000/getmove/${level}`,{
            method:'POST',
            body: JSON.stringify(boardtemp),
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
            }
        })
        .then(response=>response.json())
        .then(data=>{
            if(data!=null){
                boardtemp[data[0]][data[1]]= 2;
                setBoardgame(boardtemp)
                if(finalState(boardtemp)){
                    setGameActive(false)
                    console.log("You Lose!")
                    saveMatchResult(false)
                }
                setCurrentPlay(1)
            }
        })
    }

    function finalState(squares) {
        const ROWS = squares.length; // Số hàng
        const COLS = squares[0].length; // Số cột
        const directions = [[0, 1], [1, 0], [1, 1], [-1, 1]];
        for (let row = 0; row < ROWS; row++) {
          for (let col = 0; col < COLS; col++) {
            if (squares[row][col] !== 0) {
              const currentPlayer = squares[row][col];
              for (const [dr, dc] of directions) {
                let count = 1;
                for (let i = 1; i < 5; i++) {
                    let r = row + i * dr;
                    let c = col + i * dc;
                    if (r >= 0 && r < ROWS && c >= 0 && c < COLS && squares[r][c] === currentPlayer) {
                        count++;
                    } else {
                        break;
                    }
                }
                for (let i = 1; i < 5; i++) {
                    let r = row - i * dr;
                    let c = col - i * dc;
                    if (r >= 0 && r < ROWS && c >= 0 && c < COLS && squares[r][c] === currentPlayer) {
                        count++;
                    } else {
                        break;
                    }
                }
                if (count >= 5) {
                  return true;
                }
              }
            }
          }
        }
        return false;
    }
      
    function rePlay(){
        setBoardgame(Array.from({ length: rows }, () =>Array.from({ length: cols }, () => 0)))
        setGameActive(true)
        setStartTime(null)
        setCurrentPlay(1)
    }

    function saveMatchResult(win){
        const elapsedSeconds = Math.round((performance.now() - startTime) / 1000)
        console.log(elapsedSeconds)
        fetch(`http://127.0.0.1:5001/insertmatch`,{
            method:'POST',
            body: JSON.stringify({
                userID: user.id,
                score: elapsedSeconds,
                status: win ? 1 : 0,
            }),
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
            }
        })
        setImgend(imglose)
        if(win){
            fetch(`http://127.0.0.1:5001/updatehighscore`,{
                method:'POST',
                body: JSON.stringify({
                    userID: user.id,
                    score: elapsedSeconds,
                }),
                headers: {
                    'Content-Type': 'application/json; charset=UTF-8',
                }
            })
            setImgend(imgwin)
        }
    }
    // console.log(boardgame)
    return (
        <div className="grid">
            <div className="playing-heading">
                <Link to="/" className="playing-btnBack"><i className="fa-solid fa-reply"></i></Link>
                <h1 className='playing-user'>{"User: "+user.username}</h1>
                <div onClick={rePlay} className="playing-btnReplay"><i className="fa-solid fa-rotate-right"></i></div>
            </div>
            <div className="boardgame">
            {
                boardgame.map((row,rowIndex)=>{
                    return(
                        row.map((col,colIndex)=>{
                        return(
                            <div 
                                key={rowIndex+" "+colIndex} 
                                onClick={(e)=>cellClicked(e,rowIndex,colIndex)} 
                                className={col==1? "cell x":col==2? "cell o":"cell"}
                            >
                            {col==1 ? "X":col==2? "O":""}
                            </div>
                        )
                        })
                    )
                })
            }
            <img style={gameActive? {display:"none"}:{}} className='img-end' src={imgend} alt="" />
            </div>
        </div>
    );
}

export default Playing;
