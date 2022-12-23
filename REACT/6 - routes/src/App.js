import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import './App.css';
import Autoria from './components/Autoria';
import Calculator from './components/Calculator';

function App() {
  return (
    <div className="App">
      <Calculator />
      <Router>
        <ul>
          <li><Link to="/autoria">Clique aqui para visualizar as informações autorais</Link></li>
        </ul>
        <Routes>
          <Route path="/autoria" element={<Autoria />} />
        </Routes>
      </Router>
    </div>

  );
}

export default App;
