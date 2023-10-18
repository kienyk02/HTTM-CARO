import React from 'react'
import Models from './Models'
import Model from './Model'
import { Route, Routes } from 'react-router-dom'

function App() {
    return (
      <React.Fragment>
        <Routes>
            <Route path='/models' element={<Models/>}/>
            <Route path='/model/:id' element={<Model/>}/>
        </Routes>
      </React.Fragment>
    )
}

export default App
