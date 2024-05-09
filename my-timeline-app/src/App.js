import React from 'react';
import Timeline from './components/Timeline';
import './App.css';

const timelineData = [
  { year: "17' 05", title: 'Poincaré Embeddings' },
  // 他の論文データを追加...
];

const App = () => (
  <div className="App">
    <h1>Research Timeline</h1>
    <Timeline items={timelineData} />
  </div>
);

export default App;