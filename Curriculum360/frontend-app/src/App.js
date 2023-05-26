import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.css'
import './App.css';
import navbarx from './components/navbar';


function App() {
  return (
    <div className="App">
      <div><navbarx /></div>
      <h1>Hello developers this is the setup of our SRE project</h1>
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
