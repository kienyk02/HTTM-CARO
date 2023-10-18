import {Route,Routes} from 'react-router-dom'
import Playing from './Playing'
import Home from './Home'

function App() {
  return (
    <Routes>
        <Route path='/' element={<Home/>} />
        <Route path='play/:level' element={<Playing/>} />
    </Routes>
  )
}

export default App
