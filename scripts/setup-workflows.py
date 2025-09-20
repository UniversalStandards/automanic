#!/usr/bin/env python3
"""
GitHub Workflows Setup Script

Creates GitHub Actions workflows based on project configuration.
"""

import os
import json
from pathlib import Path
from typing import Dict

class WorkflowGenerator:
    """Generates GitHub Actions workflows based on configuration"""
    
    def __init__(self, config_file: str = 'README.md'):
        self.config = self._parse_config(config_file)
        
    def _parse_config(self, config_file: str) -> Dict[str, str]:
        """Parse configuration from README.md"""
        # For now, return a default config - in practice this would parse the README
        return {
            'PROJECT_TYPE': 'web-app',
            'LANGUAGE': 'python',
            'FRAMEWORK': 'fastapi',
            'BUILD_SYSTEM': 'pip',
            'TESTING': 'pytest',
            'CI_CD': 'github-actions',
            'DEPLOYMENT': 'docker'
        }
        
    def generate_workflows(self):
        """Generate all necessary workflows"""
        workflows_dir = Path('.github/workflows')
        workflows_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate CI workflow
        self._generate_ci_workflow()
        
        # Generate CD workflow
        self._generate_cd_workflow()
        
        # Generate security workflow
        self._generate_security_workflow()
        
        # Generate dependency update workflow
        self._generate_dependabot_workflow()
        
        print("✅ GitHub Actions workflows generated!")
        
    def _generate_ci_workflow(self):
        """Generate Continuous Integration workflow"""
        language = self.config.get('LANGUAGE', 'python')
        testing = self.config.get('TESTING', 'pytest')
        
        if language == 'python':
            ci_workflow = {
                'name': 'CI',
                'on': {
                    'push': {'branches': ['main', 'develop']},
                    'pull_request': {'branches': ['main']}
                },
                'jobs': {
                    'test': {
                        'runs-on': 'ubuntu-latest',
                        'strategy': {
                            'matrix': {
                                'python-version': ['3.8', '3.9', '3.10', '3.11']
                            }
                        },
                        'steps': [
                            {
                                'uses': 'actions/checkout@v4'
                            },
                            {
                                'name': 'Set up Python',
                                'uses': 'actions/setup-python@v4',
                                'with': {
                                    'python-version': '${{ matrix.python-version }}'
                                }
                            },
                            {
                                'name': 'Install dependencies',
                                'run': 'pip install -r requirements.txt'
                            },
                            {
                                'name': 'Lint with flake8',
                                'run': '''
                                    pip install flake8
                                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                                    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
                                '''.strip()
                            },
                            {
                                'name': 'Test with pytest',
                                'run': '''
                                    pip install pytest pytest-cov
                                    pytest --cov=./ --cov-report=xml
                                '''.strip()
                            },
                            {
                                'name': 'Upload coverage reports',
                                'uses': 'codecov/codecov-action@v3',
                                'with': {
                                    'file': './coverage.xml',
                                    'flags': 'unittests',
                                    'name': 'codecov-umbrella',
                                    'fail_ci_if_error': True
                                }
                            }
                        ]
                    }
                }
            }
        elif language in ['javascript', 'typescript']:
            ci_workflow = {
                'name': 'CI',
                'on': {
                    'push': {'branches': ['main', 'develop']},
                    'pull_request': {'branches': ['main']}
                },
                'jobs': {
                    'test': {
                        'runs-on': 'ubuntu-latest',
                        'strategy': {
                            'matrix': {
                                'node-version': ['16', '18', '20']
                            }
                        },
                        'steps': [
                            {
                                'uses': 'actions/checkout@v4'
                            },
                            {
                                'name': 'Use Node.js',
                                'uses': 'actions/setup-node@v3',
                                'with': {
                                    'node-version': '${{ matrix.node-version }}',
                                    'cache': 'npm'
                                }
                            },
                            {
                                'name': 'Install dependencies',
                                'run': 'npm ci'
                            },
                            {
                                'name': 'Run linter',
                                'run': 'npm run lint'
                            },
                            {
                                'name': 'Run tests',
                                'run': 'npm test'
                            },
                            {
                                'name': 'Build project',
                                'run': 'npm run build'
                            }
                        ]
                    }
                }
            }
        else:
            # Generic CI workflow
            ci_workflow = {
                'name': 'CI',
                'on': {
                    'push': {'branches': ['main', 'develop']},
                    'pull_request': {'branches': ['main']}
                },
                'jobs': {
                    'test': {
                        'runs-on': 'ubuntu-latest',
                        'steps': [
                            {
                                'uses': 'actions/checkout@v4'
                            },
                            {
                                'name': 'Run tests',
                                'run': 'echo "Add your test commands here"'
                            }
                        ]
                    }
                }
            }
            
        self._write_workflow('ci.yml', ci_workflow)
        
    def _generate_cd_workflow(self):
        """Generate Continuous Deployment workflow"""
        deployment = self.config.get('DEPLOYMENT', 'none')
        
        cd_workflow = {
            'name': 'CD',
            'on': {
                'push': {'branches': ['main']},
                'release': {'types': ['published']}
            },
            'jobs': {
                'deploy': {
                    'runs-on': 'ubuntu-latest',
                    'needs': 'test',
                    'steps': [
                        {
                            'uses': 'actions/checkout@v4'
                        }
                    ]
                }
            }
        }
        
        if deployment == 'docker':
            cd_workflow['jobs']['deploy']['steps'].extend([
                {
                    'name': 'Set up Docker Buildx',
                    'uses': 'docker/setup-buildx-action@v3'
                },
                {
                    'name': 'Login to DockerHub',
                    'uses': 'docker/login-action@v3',
                    'with': {
                        'username': '${{ secrets.DOCKERHUB_USERNAME }}',
                        'password': '${{ secrets.DOCKERHUB_TOKEN }}'
                    }
                },
                {
                    'name': 'Build and push',
                    'uses': 'docker/build-push-action@v5',
                    'with': {
                        'context': '.',
                        'push': True,
                        'tags': 'user/app:latest'
                    }
                }
            ])
        elif deployment == 'vercel':
            cd_workflow['jobs']['deploy']['steps'].extend([
                {
                    'name': 'Deploy to Vercel',
                    'uses': 'amondnet/vercel-action@v25',
                    'with': {
                        'vercel-token': '${{ secrets.VERCEL_TOKEN }}',
                        'vercel-org-id': '${{ secrets.ORG_ID }}',
                        'vercel-project-id': '${{ secrets.PROJECT_ID }}',
                        'vercel-args': '--prod'
                    }
                }
            ])
        else:
            cd_workflow['jobs']['deploy']['steps'].append({
                'name': 'Deploy',
                'run': 'echo "Add your deployment commands here"'
            })
            
        self._write_workflow('cd.yml', cd_workflow)
        
    def _generate_security_workflow(self):
        """Generate security scanning workflow"""
        security_workflow = {
            'name': 'Security',
            'on': {
                'push': {'branches': ['main']},
                'pull_request': {'branches': ['main']},
                'schedule': [{'cron': '0 6 * * 1'}]  # Weekly on Mondays
            },
            'jobs': {
                'analyze': {
                    'name': 'Analyze',
                    'runs-on': 'ubuntu-latest',
                    'permissions': {
                        'actions': 'read',
                        'contents': 'read',
                        'security-events': 'write'
                    },
                    'strategy': {
                        'fail-fast': False,
                        'matrix': {
                            'language': [self.config.get('LANGUAGE', 'python')]
                        }
                    },
                    'steps': [
                        {
                            'name': 'Checkout repository',
                            'uses': 'actions/checkout@v4'
                        },
                        {
                            'name': 'Initialize CodeQL',
                            'uses': 'github/codeql-action/init@v2',
                            'with': {
                                'languages': '${{ matrix.language }}'
                            }
                        },
                        {
                            'name': 'Autobuild',
                            'uses': 'github/codeql-action/autobuild@v2'
                        },
                        {
                            'name': 'Perform CodeQL Analysis',
                            'uses': 'github/codeql-action/analyze@v2'
                        }
                    ]
                }
            }
        }
        
        self._write_workflow('security.yml', security_workflow)
        
    def _generate_dependabot_workflow(self):
        """Generate dependabot configuration"""
        language = self.config.get('LANGUAGE', 'python')
        
        package_ecosystems = {
            'python': 'pip',
            'javascript': 'npm',
            'typescript': 'npm',
            'go': 'gomod',
            'rust': 'cargo',
            'java': 'maven'
        }
        
        dependabot_config = {
            'version': 2,
            'updates': [
                {
                    'package-ecosystem': package_ecosystems.get(language, 'pip'),
                    'directory': '/',
                    'schedule': {
                        'interval': 'weekly',
                        'day': 'monday'
                    },
                    'open-pull-requests-limit': 10
                },
                {
                    'package-ecosystem': 'github-actions',
                    'directory': '/',
                    'schedule': {
                        'interval': 'weekly'
                    }
                }
            ]
        }
        
        dependabot_dir = Path('.github')
        dependabot_dir.mkdir(exist_ok=True)
        
        with open(dependabot_dir / 'dependabot.yml', 'w') as f:
            import yaml
            yaml.dump(dependabot_config, f, default_flow_style=False)
            
    def _write_workflow(self, filename: str, workflow: dict):
        """Write workflow to YAML file"""
        import yaml
        
        workflows_dir = Path('.github/workflows')
        with open(workflows_dir / filename, 'w') as f:
            yaml.dump(workflow, f, default_flow_style=False, sort_keys=False)

def main():
    try:
        generator = WorkflowGenerator()
        generator.generate_workflows()
        print("✅ All workflows generated successfully!")
    except Exception as e:
        print(f"❌ Error generating workflows: {e}")

if __name__ == "__main__":
    main()