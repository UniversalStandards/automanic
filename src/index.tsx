// src/index.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './styles.css'; // Import the custom styles

ReactDOM.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>,
    document.getElementById('root')
);
