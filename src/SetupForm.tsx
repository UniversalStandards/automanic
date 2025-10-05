// src/SetupForm.tsx
import React, { useState } from 'react';
import { Button, TextField, Typography, Box, LinearProgress } from '@mui/material';

const questions = [
    {
        question: "What is your project's type?",
        options: ["web-app", "cli-tool", "library", "api", "mobile-app", "desktop-app", "data-science", "documentation"],
        type: "select"
    },
    {
        question: "What programming language will you use?",
        options: ["python", "javascript", "typescript", "go", "rust", "java", "cpp", "c", "php", "ruby", "swift", "kotlin", "scala", "r"],
        type: "select"
    },
    {
        question: "What framework do you plan to use?",
        options: ["react", "vue", "angular", "express", "fastapi", "django", "spring", "gin", "actix", "electron", "flutter", "pytorch", "tensorflow", "none"],
        type: "select"
    },
    {
        question: "What build system will you use?",
        options: ["npm", "yarn", "pip", "cargo", "maven", "gradle", "make", "cmake", "none"],
        type: "select"
    },
    {
        question: "What database will you use?",
        options: ["postgresql", "mysql", "mongodb", "redis", "sqlite", "none"],
        type: "select"
    },
];

const SetupForm: React.FC = () => {
    const [currentStep, setCurrentStep] = useState(0);
    const [answers, setAnswers] = useState<string[]>(Array(questions.length).fill(''));
    
    const handleNext = () => {
        if (currentStep < questions.length - 1) {
            setCurrentStep(currentStep + 1);
        } else {
            console.log("Final Answers:", answers);
            // Here you would handle form submission
        }
    };

    const handleChange = (value: string) => {
        const updatedAnswers = [...answers];
        updatedAnswers[currentStep] = value;
        setAnswers(updatedAnswers);
    };

    const progress = ((currentStep + 1) / questions.length) * 100;

    return (
        <Box sx={{ width: '100%', padding: 4 }}>
            <Typography variant="h4" gutterBottom>
                Automanic Project Setup
            </Typography>
            <LinearProgress variant="determinate" value={progress} />
            <Typography variant="body1" sx={{ margin: '10px 0' }}>
                Question {currentStep + 1} of {questions.length}
            </Typography>
            <Typography variant="h6" gutterBottom>
                {questions[currentStep].question}
            </Typography>
            {questions[currentStep].type === "select" && (
                <TextField
                    select
                    fullWidth
                    label="Select an option"
                    value={answers[currentStep]}
                    onChange={(e) => handleChange(e.target.value)}
                    SelectProps={{
                        native: true,
                    }}
                    variant="outlined"
                    sx={{ marginBottom: 2 }}
                >
                    <option value="" disabled>Select an option</option>
                    {questions[currentStep].options.map((option, index) => (
                        <option key={index} value={option}>{option}</option>
                    ))}
                </TextField>
            )}
            <Button variant="contained" onClick={handleNext} disabled={!answers[currentStep]}>
                {currentStep < questions.length - 1 ? "Next" : "Finish"}
            </Button>
        </Box>
    );
};

export default SetupForm;
