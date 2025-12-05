import React, { useState, useCallback } from 'react';
import {
    Button,
    TextField,
    Typography,
    Box,
    LinearProgress,
    Paper,
    Stepper,
    Step,
    StepLabel,
    Alert,
    Card,
    CardContent,
    Chip,
    Stack,
    Divider
} from '@mui/material';

interface Question {
    question: string;
    options: string[];
    type: string;
    key: string;
    description: string;
}

const questions: Question[] = [
    {
        key: "PROJECT_TYPE",
        question: "What type of project are you creating?",
        description: "Select the primary purpose of your project",
        options: ["web-app", "cli-tool", "library", "api", "mobile-app", "desktop-app", "data-science", "documentation"],
        type: "select"
    },
    {
        key: "LANGUAGE",
        question: "What programming language will you use?",
        description: "Choose your primary programming language",
        options: ["python", "javascript", "typescript", "go", "rust", "java", "cpp", "c", "php", "ruby", "swift", "kotlin", "scala", "r"],
        type: "select"
    },
    {
        key: "FRAMEWORK",
        question: "What framework do you plan to use?",
        description: "Select a framework or 'none' if not applicable",
        options: ["react", "vue", "angular", "express", "fastapi", "django", "spring", "gin", "actix", "electron", "flutter", "pytorch", "tensorflow", "none"],
        type: "select"
    },
    {
        key: "BUILD_SYSTEM",
        question: "What build system will you use?",
        description: "Choose your package manager and build tool",
        options: ["npm", "yarn", "pip", "cargo", "maven", "gradle", "make", "cmake", "none"],
        type: "select"
    },
    {
        key: "DATABASE",
        question: "What database will you use?",
        description: "Select a database or 'none' if not needed",
        options: ["postgresql", "mysql", "mongodb", "redis", "sqlite", "none"],
        type: "select"
    },
    {
        key: "DEPLOYMENT",
        question: "How will you deploy your project?",
        description: "Choose your deployment platform",
        options: ["docker", "kubernetes", "aws", "gcp", "azure", "vercel", "netlify", "heroku", "none"],
        type: "select"
    },
    {
        key: "CI_CD",
        question: "What CI/CD system will you use?",
        description: "Select your continuous integration platform",
        options: ["github-actions", "jenkins", "gitlab-ci", "circleci", "travis-ci", "none"],
        type: "select"
    },
    {
        key: "TESTING",
        question: "What testing framework will you use?",
        description: "Choose your testing framework",
        options: ["jest", "pytest", "cargo-test", "junit", "go-test", "rspec", "none"],
        type: "select"
    },
    {
        key: "LICENSE_TYPE",
        question: "What license will you use?",
        description: "Select a license for your project",
        options: ["mit", "apache-2.0", "gpl-v3", "bsd-3-clause", "unlicense", "proprietary"],
        type: "select"
    },
    {
        key: "VISIBILITY",
        question: "Will this be a public or private repository?",
        description: "Choose repository visibility",
        options: ["public", "private"],
        type: "select"
    },
];

const SetupForm: React.FC = () => {
    const [currentStep, setCurrentStep] = useState(0);
    const [answers, setAnswers] = useState<Record<string, string>>({});
    const [isComplete, setIsComplete] = useState(false);
    const [generatedConfig, setGeneratedConfig] = useState<string>('');

    const handleNext = useCallback(() => {
        if (currentStep < questions.length - 1) {
            setCurrentStep(currentStep + 1);
        } else {
            generateConfiguration();
            setIsComplete(true);
        }
    }, [currentStep, answers]);

    const handleBack = useCallback(() => {
        if (currentStep > 0) {
            setCurrentStep(currentStep - 1);
        }
    }, [currentStep]);

    const handleChange = useCallback((value: string) => {
        setAnswers(prev => ({
            ...prev,
            [questions[currentStep].key]: value
        }));
    }, [currentStep]);

    const generateConfiguration = useCallback(() => {
        const configLines = [
            '<!-- AUTOMANIC-CONFIG-START -->',
            ...questions.map(q => `${q.key}: ${answers[q.key] || 'none'}`),
            '<!-- AUTOMANIC-CONFIG-END -->'
        ];
        setGeneratedConfig(configLines.join('\n'));
    }, [answers]);

    const handleCopyToClipboard = useCallback(() => {
        navigator.clipboard.writeText(generatedConfig);
    }, [generatedConfig]);

    const handleReset = useCallback(() => {
        setCurrentStep(0);
        setAnswers({});
        setIsComplete(false);
        setGeneratedConfig('');
    }, []);

    const progress = ((currentStep + 1) / questions.length) * 100;
    const currentQuestion = questions[currentStep];

    if (isComplete) {
        return (
            <Paper elevation={3} sx={{ p: 4 }}>
                <Typography variant="h4" gutterBottom color="primary">
                    🎉 Configuration Complete!
                </Typography>
                <Alert severity="success" sx={{ mb: 3 }}>
                    Your Automanic configuration has been generated successfully.
                </Alert>

                <Typography variant="h6" gutterBottom>
                    Your Configuration:
                </Typography>

                <Card variant="outlined" sx={{ mb: 3, bgcolor: 'grey.50' }}>
                    <CardContent>
                        <Stack direction="row" spacing={1} flexWrap="wrap" sx={{ mb: 2 }}>
                            {Object.entries(answers).map(([key, value]) => (
                                <Chip key={key} label={`${key}: ${value}`} size="small" color="primary" variant="outlined" />
                            ))}
                        </Stack>
                        <Divider sx={{ my: 2 }} />
                        <pre style={{ overflow: 'auto', fontSize: '0.875rem', margin: 0 }}>
                            {generatedConfig}
                        </pre>
                    </CardContent>
                </Card>

                <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                    Copy this configuration block and paste it into your README.md file, then run:
                </Typography>

                <Card variant="outlined" sx={{ mb: 3, bgcolor: 'grey.900' }}>
                    <CardContent>
                        <code style={{ color: '#4caf50' }}>./scripts/setup.sh</code>
                    </CardContent>
                </Card>

                <Stack direction="row" spacing={2}>
                    <Button variant="contained" onClick={handleCopyToClipboard}>
                        Copy Configuration
                    </Button>
                    <Button variant="outlined" onClick={handleReset}>
                        Start Over
                    </Button>
                </Stack>
            </Paper>
        );
    }

    return (
        <Paper elevation={3} sx={{ p: 4 }}>
            <Typography variant="h4" gutterBottom color="primary">
                🚀 Automanic Project Setup
            </Typography>
            <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
                Configure your project by answering a few questions. This will generate
                the configuration block for your README.md file.
            </Typography>

            <Stepper activeStep={currentStep} alternativeLabel sx={{ mb: 4 }}>
                {questions.map((q, index) => (
                    <Step key={q.key}>
                        <StepLabel>{index === currentStep ? q.key.replace('_', ' ') : ''}</StepLabel>
                    </Step>
                ))}
            </Stepper>

            <LinearProgress variant="determinate" value={progress} sx={{ mb: 3, height: 8, borderRadius: 4 }} />

            <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                Question {currentStep + 1} of {questions.length}
            </Typography>

            <Typography variant="h5" gutterBottom>
                {currentQuestion.question}
            </Typography>

            <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                {currentQuestion.description}
            </Typography>

            <TextField
                select
                fullWidth
                label="Select an option"
                value={answers[currentQuestion.key] || ''}
                onChange={(e) => handleChange(e.target.value)}
                SelectProps={{
                    native: true,
                }}
                variant="outlined"
                sx={{ mb: 3 }}
            >
                <option value="" disabled>Select an option</option>
                {currentQuestion.options.map((option, index) => (
                    <option key={index} value={option}>{option}</option>
                ))}
            </TextField>

            <Stack direction="row" spacing={2} justifyContent="space-between">
                <Button
                    variant="outlined"
                    onClick={handleBack}
                    disabled={currentStep === 0}
                >
                    Back
                </Button>
                <Button
                    variant="contained"
                    onClick={handleNext}
                    disabled={!answers[currentQuestion.key]}
                >
                    {currentStep < questions.length - 1 ? "Next" : "Generate Configuration"}
                </Button>
            </Stack>
        </Paper>
    );
};

export default SetupForm;
