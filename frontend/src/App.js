import './App.css';
import logo from "./logo.svg";
import axios from 'axios';

function App() {
  axios.get("http://localhost:5000").then(res => {
    console.log(res);
  }).catch(err => {
    console.log(err)
  })
  const companies = ["楽天株式会社", "LINE株式会社", "株式会社VOYAGE", "メルカリ"];
  const siteURLs = ["", "", "https://voyagegroup.snar.jp/", ""]
  const internURLs = ["","","","https://mercan.mercari.com/articles/28040/"]
  const showCompany = companies.map((element, i) => 
  <div className="cardWrapper">
  <div className="card" key={i}>
    <img class="card-img" src={logo} alt=""></img>
      <div className="card-content">
        <h1 className="card-title">{element}</h1>
      </div>
    <div className="card-link">
    <a href={siteURLs[i]}>About</a>
    <a href={internURLs[i]}>Website</a>
    </div>
  </div>
  </div>
)
  return (
    <div className="App">
      <header className="App-header">
        <h1> Internship infomation center </h1>
      </header>
      <div>
        {showCompany}
      </div>
    </div>
  );
}

export default App;
