// src/App.tsx
import React from 'react';
import SetupForm from './SetupForm';
import { CssBaseline, Container } from '@mui/material';

const App: React.FC = () => {
    return (
        <Container component="main" maxWidth="xs">
            <CssBaseline />
            <SetupForm />
        </Container>
    );
};

export default App;
