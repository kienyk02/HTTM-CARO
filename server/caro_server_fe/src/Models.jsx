import React, { useEffect,useState } from 'react'
import { Link } from 'react-router-dom'
import "./assets/css/style.css"
let models_default=[]
function Models() {
    const [models,setModels]=useState([])
    const [selected,setSelected]=useState(0)
    
    function loadModels(){
        fetch("http://127.0.0.1:5000/getmodels")
        .then((response)=>response.json())
        .then(data=>{
            models_default=[...data]
            setModels(data)
        })
        .catch(err=> console.log(err))
    }
    useEffect(()=>{
        loadModels()
    },[])
    function handleSearch(e){
        setModels(
            models_default.filter((model)=>{
                return model.name.toLowerCase().includes(e.target.value.toLowerCase()) 
                || model.link.toLowerCase().includes(e.target.value.toLowerCase()) 
            })
        )
    }
    function onDelete(id){
        if(window.confirm(`Do you want to delete Model with id ${id}`))
        {
            fetch(`http://127.0.0.1:5000/deletemodel/${id}`,{method: 'Delete'})
            setModels(models.filter(model => model.id!=id))
        }
    }
    function handleActiveBtn(){
        if(selected>0){
            fetch(`http://127.0.0.1:5000/activemodel/${selected}`)
            .then((response)=>response.json())
            .then(data=>{
                setModels([])
                loadModels()
            })
        }else{
            alert("Vui lòng chọn model!")
        }
    }

    return (
    <div className="grid">
        <h2 className="text-center" style={{paddingTop:"10px"}}>Models</h2>
        <div className="select-model">
            <label htmlFor="">Active Model</label>
            <select className='select-list' value={selected} onChange={(e)=>setSelected(e.target.value)}>
                <option value={0}>--Select Model--</option>
                {
                    models.map((model)=>{
                        return(
                            <option key={model.id} value={model.id}>{model.name}</option>
                        )
                    })
                }
            </select>
            <div onClick={handleActiveBtn} className="btn btn-primary">Active</div>
        </div>
        <div style={{display:'flex', justifyContent:'space-between'}} className="row">
            <input 
                style={{height:'40px',width:'300px',padding:'10px',border: '1px solid #ccc',fontSize:'18px',borderRadius:'5px'}} 
                onChange={(e)=>handleSearch(e)}  type="text"
                placeholder='Enter name or link'
            />
            <Link to="/model/-1">
                <button className="btn btn-primary">
                Add Model
                </button>
            </Link>
        </div>
        <div className="row">
            <table className="table table-striped table-bordered">
                <thead className="table-dark">
                    <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>LINK</th>
                    <th>EASY</th>
                    <th>MEDIUM</th>
                    <th>HARD</th>
                    <th>ACTIVE</th>
                    <th>ACTION</th>
                    </tr>
                </thead>
                <tbody >
                    {
                    models.map(model=>
                    (
                    <tr key={model.id}>
                        <td>{model.id}</td>
                        <td>{model.name}</td>
                        <td>{model.link}</td>
                        <td>{model.easy}</td>
                        <td>{model.medium}</td>
                        <td>{model.hard}</td>
                        <td>
                            <input disabled style={{ width: '25px', height: '25px' }} type="checkbox" 
                            defaultChecked={model.action=="enable" ? true:false}/>
                        </td>
                        <td style={{display:'flex', justifyContent:'space-evenly'}}>
                            <Link to={`/model/${model.id}`} className="btn btn-info">Update</Link>
                            <button onClick={()=>onDelete(model.id)} className="btn btn-danger">Delete</button>
                        </td>
                    </tr>
                    )
                    )
                    }
                </tbody>
            </table>
        </div>
        <Link style={{marginRight:'5px', alignSelf:'end',width:'110px'}} to="/" className='btn btn-secondary'>Back</Link>
    </div>
    )
}

export default Models