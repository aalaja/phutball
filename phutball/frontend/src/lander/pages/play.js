import React from 'react';
import API from '../../api'

export default class Play extends React.Component {
  render() {
    return (
      <div className="content">
        <div id="sub" className="subtitle" key="a">
          Version 0.1 (May 8, 2020)
        </div>
        <div id="content" className="text" key="b">
          <p id="1">
          philosophers.football currently only supports playing against another
          real-life person on the same computer. Workarounds are available however:</p>
          <ul>
            <li id="3">
          Future versions will include bots you can play against!
            </li>
          <li id="2"> If you want to play against another real-life person who will use a
          different computer, you can play pseudo-asynchronously by
          starting a game and sending them the URL to the game, which
          contains the unique game ID.</li>
          </ul>
          <p id="4">
          If playing on different computers, be warned:
            <ul>
              <li key="1"> There is no authentication &ndash; nothing stops a
              third party from interfering in your game by impersonating you,
              or stops your opponent from playing as you. However, you
              can always and easily undo moves.
              </li><li key="3">Note: The Game IDs are sufficiently unique
              that an attacker is unlikely to guess yours; hence the 
              philosophers.football equivalent of Zoom-bombing is unlikely.</li>
              <li key="2"> You and your opponent will have to refresh the 
              page manually to check for new moves.</li>
            </ul>
          </p>

        </div>
        <div id="creator" className="creator" key="c">
          <GameCreator/>
        </div>
        <div id="content" className="text" key="d">
          <p>
          Looking to resume a previous game? All games are saved if
          you played online! Just find a URL like philosophers.football/game/ABC123 in your browser history.
          </p>
        </div>
      </div>
    );
  }
};




class GameCreator extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      player0Name : '',
      player1Name : '',
      requestSent : false,
    }

    this.handlePlayer0Change = this.handlePlayer0Change.bind(this);
    this.handlePlayer1Change = this.handlePlayer1Change.bind(this)
    this.handleSubmit        = this.handleSubmit.bind(this);

    this.api = new API()

  }

  handlePlayer0Change(event) {
    if (this.state.requestSent) {
      event.preventDefault()
    } else {
      this.setState({player0Name : event.target.value.toUpperCase()})
    }
  }

  handlePlayer1Change(event) {
    if (this.state.requestSent) {
      event.preventDefault()
    } else {
      this.setState({player1Name : event.target.value.toUpperCase()})
    }
  }

  handleSubmit(event) {
    event.preventDefault()
    const gameParams = {
      'player_0_name' : this.state.player0Name,
      'player_1_name' : this.state.player1Name
    }

    this.setState({requestSent : true})
    this.api.createGame(gameParams).then(gameID => (window.location.href=`/game/${gameID}`))
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label key="1" className="input">
          Player 1 (X's) <input type="text" id="player0"
            value={this.state.player0Name} 
            onChange={this.handlePlayer0Change}
          />
        </label>
        <br/>
        <label key="2" className="input">
          Player 2 (O's) <input type="text" id="player1"
            value={this.state.player1Name} 
            onChange={this.handlePlayer1Change}
          />
        </label><br/>
        <input className="submit" type="submit" value={this.state.requestSent ? 'Preparing your game' : 'Get Started!'}/>
      </form>
    )
  } 
}