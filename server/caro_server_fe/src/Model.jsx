import React,{useEffect,useState} from "react"
import { useParams,Link } from "react-router-dom"
import { useNavigate } from "react-router-dom";
function Model(){
    const [model,setModel]=useState({
        id: '',
        name: '', 
        link: '', 
        easy: '', 
        medium:'',
        hard:'',
        action: '',
    })
    const params=useParams()
    const id=params.id
    const navigate = useNavigate();
    useEffect(()=>{
        fetch(`http://127.0.0.1:5000/getmodel/${id}`)
        .then(response=>response.json())
        .then(data=>setModel(data))
        .catch(err=>console.log(err))
    },[])
    const onSaveClick=(e)=>{
        e.preventDefault()
        fetch(`http://127.0.0.1:5000/savemodel/${id}`,
        {
            method: 'POST',
            mode:'cors',
            body: JSON.stringify(model),
            headers: {
                'Content-Type': 'application/json; charset=UTF-8',
            }
        }
        )
        .then(response=>response.json())
        .then(data=> {
            if(data){
                navigate('/models')
            }
        })
        .catch(err=>console.log(err))   
    }
    
    
    return(
        <div className="grid">
            <form onSubmit={onSaveClick} className="model-form">       
                <h1>{id < 0 ? "New Model" : `Model ${id}`}</h1>
                <input hidden type="number" value={model.id} 
                    onChange={(e)=>setModel({...model,id:e.target.value})} />
                <br/>
                <label >Name</label>
                <input required type="text" value={model.name}
                    onChange={e => setModel({ ...model, name: e.target.value })} />
                <br />
                <label >Link</label>
                <input required type="text" value={model.link}
                    onChange={e => setModel({ ...model, link: e.target.value })} />
                <br />
                <label >Easy Depth</label>
                <input required type="text" value={model.easy}
                    onChange={e => setModel({ ...model, easy: e.target.value })} />
                <br />
                <label >Medium Depth</label>
                <input required type="text" value={model.medium}
                    onChange={e => setModel({ ...model, medium: e.target.value })} />
                <br />
                <label >Hard Depth</label>
                <input required type="text" value={model.hard}
                    onChange={e => setModel({ ...model, hard: e.target.value })} />
                <br />
                <input hidden type="checkbox" checked={model.action=="enable"? true:false}
                    onChange={e => setModel({ ...model, action: e.target.checked ? 'enable':'disable' })} />
                <br />
                <div style={{display:'flex',justifyContent:'space-between'}}>
                    <button type="submit" className="btn btn-primary" >Save model</button>
                    <Link to="/models" className="btn btn-secondary" style={{width:'150px'}}>Back</Link>
                </div>
            </form>
        </div>
    )
}
export default Model