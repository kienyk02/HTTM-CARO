import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import "./assets/css/home.css"

function Home() {
    const [user,setUser]=useState({
        id:1,
        username:"sa",
        password:"123",
        email:"",
        highScore:"8"
    })
    useEffect(()=>{
        // fetch(`http://127.0.0.1:5001/getusersession`,{credentials: 'include'})
        // .then(response=>response.json())
        // .then(data=>{
        //     console.log(data)
        //     setUser(data)
        // })
        fetch(`http://127.0.0.1:5001/getUser/39`)
        .then(response=>response.json())
        .then(data=>{
            console.log(data)
            setUser(data)
        })
    },[])
    const [level, setLevel] = useState("Easy");
    
    return (
    user!='fail' &&
    <div className="grid">
        <div style={{fontSize:'39px',color:'white',fontWeight:'bold',fontFamily:'cursive'}}>CARO GAME</div>
        <div className="menu">
            <h1 className='playing-user'>{"User: "+user.username}</h1>
            <h1 style={{color:"orange",marginBottom:"30px"}}>{"High Score: "+user.highScore}</h1>
            <Link to={`/play/${level}`} className="menu-button">Play</Link>
            <div className="dropdown menu-button">
                Level: {level}
                <div className="dropdown-content">
                    <div onClick={()=>setLevel("Easy")} className='selectlv-item'>Easy</div>
                    <div onClick={()=>setLevel("Medium")} className='selectlv-item'>Medium</div>
                    <div onClick={()=>setLevel("Hard")} className='selectlv-item'>Hard</div>
                </div>
            </div>
            <Link to="/matchhistory" className="menu-button">Match History</Link>
            <Link to="/ranking" className="menu-button">Ranking</Link>
            <Link to="logout" className="menu-button">Logout</Link>
        </div>
    </div>
    );
}

export default Home;
