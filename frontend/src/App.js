import './App.css';
import logo from "./logo.svg";
import axios from 'axios';
import React from "react"

export default class Layout extends React.Component{
  constructor(props) {
    super();
    this.state = {companies : [], siteURLs:[], internURLs:[]}
  }
  componentDidMount(e){
    axios.get("http://localhost:5000/intern").then(res => {
      this.setState({"companies":res.data["companies"], "siteURLs":res.data["siteURLs"], "internURLs":res.data["internURLs"]})
    }).catch(err => {
      console.log(err)
    })
  }

render() {
  return (
    <div className="App">
      <header className="App-header">
        <h1> Internship infomation center </h1>
      </header>
      <div>
          {this.state.companies.map((element, i) => 
          <div className="cardWrapper">
          <div className="card" key={i}>
            <img class="card-img" src={logo} alt=""></img>
              <div className="card-content">
                <h1 className="card-title">{element}</h1>
              </div>
            <div className="card-link">
            <a href={this.state.siteURLs[i]}>About</a>
            <a href={this.state.internURLs[i]}>Website</a>
            </div>
          </div>
          </div>
        )}
      </div>
    </div>
  );
}
}
