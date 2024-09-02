import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [games, setGames] = useState(null)
  const [file, setFile] = useState(null)


  useEffect(()=>{

    async function load_games(){
      
      try{
        const response = await fetch("http://127.0.0.1:8000/games")
        const data = await response.json()
        setGames(data.games)
      }catch(error){
        console.log(error)
      }

    }
    load_games()

  },[])

  async function uploadFileHandler(){
    console.log("uploading file")
    const formData = new FormData()
    formData.append("file", file)
    try{
      const response = await fetch("http://127.0.0.1:8000/upload",{
        method: "POST",
        body: formData
      })
    }catch(error){

    }
  }

  return (
    <>
      { games && <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Studio</th>
          </tr>
        </thead>
        <tbody>
          {games.map(game => {
            return <tr key={game.id}>
              <td>{game.name}</td>
              <td>{game.studio}</td>
            </tr>
          })}
        </tbody>
      </table>}
      <div>
        <label>Upload File</label>
        <input type="file" onChange={(e)=> setFile(e.target.files[0])} />
        <button onClick={uploadFileHandler}>Upload</button>
      </div>
    </>
  )
}

export default App
