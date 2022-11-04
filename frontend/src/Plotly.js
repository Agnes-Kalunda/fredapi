import React, { Component } from 'react';
import Plot from "react-plotly.js";

class Plotly extends React.Component {
    constructor(props){
        super(props);
        this.state = {data: []}
    }
    

    // defining backend fetch
    componentDidMount(){
        fetch('http://127.0.0.1:8000',{
            credentials: 'include'
        })
            .then(response => response.json())
            .then(response => this.setState({'array1': response.array1})
            )
    }

    render(){
        return (
            <div>
                <Plot
                
                    data={[
                        {type: 'scatter',
                         mode: 'lines',
                         x : [],
                         y:[],
                         marker: {color:'blue'}}
                    ]}
                    layout ={{width: 1100 , height: 800, title: 'hjgvjhkgvhvjfuj'}}
                    />

            </div>
        )
    }
}
export default Plotly;