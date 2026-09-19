/**
 * AI Career Advisor & Resume Analyzer - Frontend Engine
 * Handles user interactions, sample loading, file uploads, API requests,
 * Chart.js visualizations, and DOM updates for all 9 modules.
 */

// Application State & Configuration
const API_BASE_URL = (window.location.port === '5000' || (!window.location.port && window.location.protocol.startsWith('http') && !window.location.hostname.includes('localhost') && !window.location.hostname.includes('127.0.0.1')))
    ? ''
    : (window.location.origin.includes(':5000') ? '' : 'http://127.0.0.1:5000');

let currentAnalysisData = null;
let selectedInterests = new Set();
let uploadedFile = null;
let samplesData = null;
let radarChartInstance = null;
let matchDoughnutInstance = null;

// Initialize on DOM Load
document.addEventListener('DOMContentLoaded', () => {
    lucide.createIcons();
    fetchSamples();
    setupEventListeners();
});

// Setup DOM Event Listeners
function setupEventListeners() {
    // Tab switching
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const targetTab = e.currentTarget.getAttribute('data-tab');
            switchTab(targetTab);
        });
    });

    // File Drag and Drop
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('resumeFileInput');

    if (dropZone && fileInput) {
        dropZone.addEventListener('click', () => fileInput.click());

        dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropZone.classList.add('dragover');
        });

        dropZone.addEventListener('dragleave', () => {
            dropZone.classList.remove('dragover');
        });

        dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropZone.classList.remove('dragover');
            if (e.dataTransfer.files.length > 0) {
                handleFileSelection(e.dataTransfer.files[0]);
            }
        });

        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                handleFileSelection(e.target.files[0]);
            }
        });
    }

    // Input mode switcher (File vs Paste Text)
    const btnFileMode = document.getElementById('btnFileMode');
    const btnTextMode = document.getElementById('btnTextMode');
    const fileUploadSection = document.getElementById('fileUploadSection');
    const textInputSection = document.getElementById('textInputSection');

    if (btnFileMode && btnTextMode) {
        btnFileMode.addEventListener('click', () => {
            btnFileMode.classList.add('bg-indigo-600', 'text-white');
            btnFileMode.classList.remove('text-slate-400');
            btnTextMode.classList.remove('bg-indigo-600', 'text-white');
            btnTextMode.classList.add('text-slate-400');
            fileUploadSection.classList.remove('hidden');
            textInputSection.classList.add('hidden');
        });

        btnTextMode.addEventListener('click', () => {
            btnTextMode.classList.add('bg-indigo-600', 'text-white');
            btnTextMode.classList.remove('text-slate-400');
            btnFileMode.classList.remove('bg-indigo-600', 'text-white');
            btnFileMode.classList.add('text-slate-400');
            fileUploadSection.classList.add('hidden');
            textInputSection.classList.remove('hidden');
        });
    }

    // Add Custom Interest tag on Enter
    const customInterestInput = document.getElementById('customInterestInput');
    if (customInterestInput) {
        customInterestInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                addCustomInterest(customInterestInput.value.trim());
                customInterestInput.value = '';
            }
        });
    }

    // Analyze button click
    const analyzeBtn = document.getElementById('analyzeBtn');
    if (analyzeBtn) {
        analyzeBtn.addEventListener('click', startAnalysis);
    }

    // Sample Resume loader
    const sampleResumeSelect = document.getElementById('sampleResumeSelect');
    if (sampleResumeSelect) {
        sampleResumeSelect.addEventListener('change', (e) => {
            loadSampleResume(e.target.value);
        });
    }

    // Sample JD loader
    const sampleJdSelect = document.getElementById('sampleJdSelect');
    if (sampleJdSelect) {
        sampleJdSelect.addEventListener('change', (e) => {
            loadSampleJd(e.target.value);
        });
    }

    // Clear / Reset button
    const resetBtn = document.getElementById('resetBtn');
    if (resetBtn) {
        resetBtn.addEventListener('click', resetAll);
    }
}

// Fetch Pre-loaded Samples
async function fetchSamples() {
    try {
        const resp = await fetch(`${API_BASE_URL}/api/samples`);
        if (resp.ok) {
            samplesData = await resp.json();
            renderInterestTags(samplesData.interests);
        }
    } catch (err) {
        console.error('Failed to load samples', err);
    }
}

// Render Selectable Interest Tags
function renderInterestTags(interests) {
    const container = document.getElementById('interestTagsContainer');
    if (!container) return;
    container.innerHTML = '';

    interests.forEach(interest => {
        const tag = document.createElement('button');
        tag.type = 'button';
        tag.className = 'text-xs px-3 py-1.5 rounded-full border border-slate-700 bg-slate-800/80 text-slate-300 hover:border-indigo-500 hover:text-white transition-all';
        tag.textContent = interest;
        tag.addEventListener('click', () => {
            toggleInterestTag(interest, tag);
        });
        container.appendChild(tag);
    });
}

function toggleInterestTag(interest, element) {
    if (selectedInterests.has(interest)) {
        selectedInterests.delete(interest);
        element.classList.remove('bg-indigo-600', 'text-white', 'border-indigo-500');
        element.classList.add('bg-slate-800/80', 'text-slate-300', 'border-slate-700');
    } else {
        selectedInterests.add(interest);
        element.classList.remove('bg-slate-800/80', 'text-slate-300', 'border-slate-700');
        element.classList.add('bg-indigo-600', 'text-white', 'border-indigo-500');
    }
}

function addCustomInterest(val) {
    if (!val || selectedInterests.has(val)) return;
    selectedInterests.add(val);
    const container = document.getElementById('interestTagsContainer');
    const tag = document.createElement('button');
    tag.type = 'button';
    tag.className = 'text-xs px-3 py-1.5 rounded-full border border-indigo-500 bg-indigo-600 text-white transition-all';
    tag.textContent = val;
    tag.addEventListener('click', () => {
        selectedInterests.delete(val);
        tag.remove();
    });
    container.appendChild(tag);
}

// Handle File Selection
function handleFileSelection(file) {
    uploadedFile = file;
    const filePreview = document.getElementById('filePreview');
    const fileNameSpan = document.getElementById('selectedFileName');
    const fileSizeSpan = document.getElementById('selectedFileSize');

    if (filePreview && fileNameSpan && fileSizeSpan) {
        fileNameSpan.textContent = file.name;
        fileSizeSpan.textContent = `${(file.size / 1024).toFixed(1)} KB`;
        filePreview.classList.remove('hidden');
    }
}

function removeSelectedFile(event) {
    if (event) event.stopPropagation();
    uploadedFile = null;
    const fileInput = document.getElementById('resumeFileInput');
    if (fileInput) fileInput.value = '';
    const filePreview = document.getElementById('filePreview');
    if (filePreview) filePreview.classList.add('hidden');
}

// Load Pre-configured Sample Resume
function loadSampleResume(key) {
    if (!samplesData || !samplesData.resumes[key]) return;
    const sample = samplesData.resumes[key];

    // Switch to text mode and populate
    document.getElementById('btnTextMode').click();
    document.getElementById('resumeTextInput').value = sample.text;

    // Show banner notification
    showToast(`Loaded sample: ${sample.title}`);
}

// Load Pre-configured Sample Job Description
function loadSampleJd(key) {
    if (!samplesData || !samplesData.job_descriptions[key]) return;
    const sample = samplesData.job_descriptions[key];
    document.getElementById('targetJdInput').value = sample.text;
    showToast(`Loaded sample job: ${sample.title}`);
}

// Start Analysis Execution
async function startAnalysis() {
    const resumeText = document.getElementById('resumeTextInput').value.trim();
    const targetJd = document.getElementById('targetJdInput').value.trim();
    const apiKey = document.getElementById('apiKeyInput')?.value.trim() || '';

    // Validation
    if (!uploadedFile && !resumeText) {
        showToast('Please upload a resume file or paste your resume text.', 'error');
        return;
    }

    // Show Loading Overlay with Step Animations
    showLoading(true);

    const formData = new FormData();
    if (uploadedFile) {
        formData.append('resume_file', uploadedFile);
    } else {
        formData.append('resume_text', resumeText);
    }
    formData.append('target_jd', targetJd);
    formData.append('interests', JSON.stringify(Array.from(selectedInterests)));
    formData.append('api_key', apiKey);

    try {
        const response = await fetch(`${API_BASE_URL}/api/analyze`, {
            method: 'POST',
            body: formData
        });

        const resData = await response.json();

        if (!response.ok || !resData.success) {
            throw new Error(resData.error || 'Analysis failed. Please check inputs.');
        }

        currentAnalysisData = resData.data;
        renderAnalysisResults(currentAnalysisData);

        // Smooth scroll to results
        document.getElementById('resultsSection').classList.remove('hidden');
        document.getElementById('resultsSection').scrollIntoView({ behavior: 'smooth' });

        showToast('Analysis completed successfully!', 'success');

    } catch (err) {
        console.error('Error during analysis:', err);
        showToast(err.message, 'error');
    } finally {
        showLoading(false);
    }
}

// Render All 9 Analysis Modules
function renderAnalysisResults(data) {
    renderCandidateHeader(data);
    renderReadinessOverview(data);
    renderResumeAnalysis(data);
    renderRecommendedRoles(data);
    renderResumeJobMatch(data);
    renderSkillAnalysis(data);
    renderMissingSkills(data);
    renderPersonalizedRoadmap(data);
    renderRecommendedProjects(data);
    renderInterviewQuestions(data);

    // Refresh Lucide Icons in newly inserted DOM
    lucide.createIcons();
}

// Top Candidate Header Bar
function renderCandidateHeader(data) {
    const candidate = data.candidate_info || {};
    document.getElementById('candidateName').textContent = candidate.name || 'Candidate Profile';

    const badgesContainer = document.getElementById('candidateContactBadges');
    badgesContainer.innerHTML = '';

    if (candidate.email) {
        badgesContainer.innerHTML += `<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs bg-slate-800 text-slate-300 border border-slate-700"><i data-lucide="mail" class="w-3.5 h-3.5 text-indigo-400"></i>${candidate.email}</span>`;
    }
    if (candidate.phone) {
        badgesContainer.innerHTML += `<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs bg-slate-800 text-slate-300 border border-slate-700"><i data-lucide="phone" class="w-3.5 h-3.5 text-emerald-400"></i>${candidate.phone}</span>`;
    }
    if (candidate.github) {
        badgesContainer.innerHTML += `<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs bg-slate-800 text-slate-300 border border-slate-700"><i data-lucide="github" class="w-3.5 h-3.5 text-purple-400"></i>${candidate.github.replace('https://', '')}</span>`;
    }
    if (candidate.linkedin) {
        badgesContainer.innerHTML += `<span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs bg-slate-800 text-slate-300 border border-slate-700"><i data-lucide="linkedin" class="w-3.5 h-3.5 text-blue-400"></i>${candidate.linkedin.replace('https://', '')}</span>`;
    }

    if (data.ai_powered) {
        document.getElementById('aiBadge').classList.remove('hidden');
    } else {
        document.getElementById('aiBadge').classList.add('hidden');
    }
}

// Module 1 & 9: Overview & Career Readiness Score
function renderReadinessOverview(data) {
    const readiness = data.readiness_score || {};
    const score = readiness.overall_score || 75;

    // Update circular score gauge
    document.getElementById('readinessScoreNumber').textContent = score;
    const circle = document.getElementById('readinessCircleProgress');
    if (circle) {
        const radius = 52;
        const circumference = 2 * Math.PI * radius;
        const offset = circumference - (score / 100) * circumference;
        circle.style.strokeDasharray = `${circumference} ${circumference}`;
        circle.style.strokeDashoffset = offset;
    }

    // Tier badge & summary
    document.getElementById('readinessTierBadge').textContent = readiness.status_tier || 'Competitive';
    document.getElementById('readinessSummaryText').textContent = readiness.summary_advice || '';
    document.getElementById('executiveSummaryText').textContent = data.resume_analysis?.summary || '';

    // Quick Wins list
    const quickWinsList = document.getElementById('quickWinsList');
    quickWinsList.innerHTML = '';
    (readiness.quick_wins || []).forEach(win => {
        quickWinsList.innerHTML += `
            <li class="flex items-start gap-2.5 text-sm text-slate-300">
                <i data-lucide="zap" class="w-4 h-4 text-amber-400 shrink-0 mt-0.5"></i>
                <span>${win}</span>
            </li>
        `;
    });

    // Render Radar Chart with Chart.js
    renderRadarChart(readiness.breakdown || {});
}

function renderRadarChart(breakdown) {
    const ctx = document.getElementById('readinessRadarChart');
    if (!ctx) return;

    if (radarChartInstance) {
        radarChartInstance.destroy();
    }

    radarChartInstance = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: ['Technical Skills', 'Resume / ATS Quality', 'Project Strength', 'Role Alignment'],
            datasets: [{
                label: 'Score / 100',
                data: [
                    breakdown.technical_competency || 70,
                    breakdown.resume_impact_ats || 65,
                    breakdown.project_strength || 75,
                    breakdown.job_alignment || 80
                ],
                backgroundColor: 'rgba(99, 102, 241, 0.25)',
                borderColor: '#6366f1',
                pointBackgroundColor: '#818cf8',
                pointBorderColor: '#ffffff',
                pointHoverBackgroundColor: '#ffffff',
                pointHoverBorderColor: '#6366f1',
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                r: {
                    angleLines: { color: 'rgba(255, 255, 255, 0.1)' },
                    grid: { color: 'rgba(255, 255, 255, 0.08)' },
                    pointLabels: {
                        color: '#94a3b8',
                        font: { size: 12, family: 'Inter' }
                    },
                    ticks: {
                        display: false,
                        stepSize: 20
                    },
                    suggestedMin: 30,
                    suggestedMax: 100
                }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}

// Module 1: Resume Analysis
function renderResumeAnalysis(data) {
    const resAnalysis = data.resume_analysis || {};
    const impact = resAnalysis.impact_metrics || {};

    // Impact score
    document.getElementById('resumeImpactScore').textContent = `${impact.impact_score || 70}/100`;
    document.getElementById('resumeWordCount').textContent = `${impact.total_words || 0} words (${impact.word_count_status || 'Optimal'})`;
    document.getElementById('actionVerbsCount').textContent = impact.strong_verbs_count || 0;
    document.getElementById('quantifiedCount').textContent = impact.quantified_count || 0;

    // Strengths
    const strengthsContainer = document.getElementById('resumeStrengthsList');
    strengthsContainer.innerHTML = '';
    (resAnalysis.strengths || []).forEach(s => {
        strengthsContainer.innerHTML += `
            <div class="flex items-start gap-2.5 text-sm text-slate-300 p-2.5 rounded-lg bg-emerald-950/20 border border-emerald-800/40">
                <i data-lucide="check-circle" class="w-4 h-4 text-emerald-400 shrink-0 mt-0.5"></i>
                <span>${s}</span>
            </div>
        `;
    });

    // Weaknesses / Red Flags
    const weaknessesContainer = document.getElementById('resumeWeaknessesList');
    weaknessesContainer.innerHTML = '';
    (resAnalysis.weaknesses || []).forEach(w => {
        weaknessesContainer.innerHTML += `
            <div class="flex items-start gap-2.5 text-sm text-slate-300 p-2.5 rounded-lg bg-amber-950/20 border border-amber-800/40">
                <i data-lucide="alert-triangle" class="w-4 h-4 text-amber-400 shrink-0 mt-0.5"></i>
                <span>${w}</span>
            </div>
        `;
    });

    // Quantified Metrics badges
    const metricsContainer = document.getElementById('detectedMetricsContainer');
    metricsContainer.innerHTML = '';
    if (impact.quantified_metrics && impact.quantified_metrics.length > 0) {
        impact.quantified_metrics.forEach(m => {
            metricsContainer.innerHTML += `<span class="px-2.5 py-1 rounded bg-indigo-950/60 border border-indigo-700/50 text-indigo-300 text-xs font-mono">${m}</span>`;
        });
    } else {
        metricsContainer.innerHTML = '<span class="text-xs text-slate-400 italic">No quantifiable metrics detected. Add numbers or % improvements.</span>';
    }

    // Strong Action Verbs badges
    const verbsContainer = document.getElementById('detectedActionVerbsContainer');
    verbsContainer.innerHTML = '';
    if (impact.strong_action_verbs && impact.strong_action_verbs.length > 0) {
        impact.strong_action_verbs.forEach(v => {
            verbsContainer.innerHTML += `<span class="px-2.5 py-1 rounded bg-emerald-950/50 border border-emerald-700/50 text-emerald-300 text-xs">${v}</span>`;
        });
    } else {
        verbsContainer.innerHTML = '<span class="text-xs text-slate-400 italic">Few strong action verbs found.</span>';
    }

    // Improved Resume Bullets (if AI enhanced or built-in formula)
    const bulletsContainer = document.getElementById('optimizedBulletsContainer');
    bulletsContainer.innerHTML = '';
    const improvedBullets = data.improved_resume_bullets || [
        {
            original_concept: "Built React frontend and integrated backend APIs",
            optimized_bullet: "Architected responsive React SPA using Tailwind CSS and RESTful endpoints, reducing page load latency by 35%."
        },
        {
            original_concept: "Handled database queries and bug fixes",
            optimized_bullet: "Optimized PostgreSQL indexes and query pipelines, decreasing peak query response times from 420ms to 75ms."
        }
    ];

    improvedBullets.forEach(b => {
        bulletsContainer.innerHTML += `
            <div class="p-3.5 rounded-lg bg-slate-800/60 border border-slate-700">
                <div class="text-xs text-slate-400 line-through mb-1.5 flex items-center gap-1.5">
                    <i data-lucide="x" class="w-3.5 h-3.5 text-rose-400"></i> ${b.original_concept}
                </div>
                <div class="text-sm text-emerald-300 font-medium flex items-start justify-between gap-2">
                    <div class="flex items-start gap-1.5">
                        <i data-lucide="arrow-right" class="w-4 h-4 text-emerald-400 shrink-0 mt-0.5"></i>
                        <span>${b.optimized_bullet}</span>
                    </div>
                    <button type="button" class="copy-btn shrink-0 text-slate-400 hover:text-white" onclick="copyText('${b.optimized_bullet.replace(/'/g, "\\'")}')" title="Copy bullet">
                        <i data-lucide="copy" class="w-4 h-4"></i>
                    </button>
                </div>
            </div>
        `;
    });
}

// Module 2: Recommended Job Roles
function renderRecommendedRoles(data) {
    const rolesContainer = document.getElementById('recommendedRolesGrid');
    rolesContainer.innerHTML = '';

    (data.recommended_roles || []).forEach((role, idx) => {
        const isTop = idx === 0;
        rolesContainer.innerHTML += `
            <div class="glass-card p-5 rounded-xl border ${isTop ? 'border-indigo-500 ring-1 ring-indigo-500/40' : 'border-slate-800'} relative">
                ${isTop ? '<span class="absolute -top-3 left-5 px-2.5 py-0.5 rounded-full text-xs font-semibold bg-gradient-to-r from-indigo-500 to-purple-500 text-white uppercase tracking-wider">Top Match</span>' : ''}
                <div class="flex items-start justify-between gap-4 mb-3">
                    <div>
                        <h4 class="text-lg font-bold text-white">${role.title}</h4>
                        <span class="text-xs text-slate-400">${role.category}</span>
                    </div>
                    <div class="text-right shrink-0">
                        <span class="text-2xl font-black ${role.confidence >= 80 ? 'text-emerald-400' : 'text-indigo-400'}">${role.confidence}%</span>
                        <div class="text-[10px] text-slate-400 uppercase tracking-wider">Match Score</div>
                    </div>
                </div>
                <p class="text-xs text-slate-300 mb-4 line-clamp-2">${role.description}</p>
                <div class="grid grid-cols-2 gap-2 text-xs mb-4 p-2.5 rounded-lg bg-slate-900/60 border border-slate-800">
                    <div>
                        <span class="text-slate-500 block">Est. Salary (US)</span>
                        <span class="font-semibold text-slate-200">${role.salary_range?.us || '$85k - $130k'}</span>
                    </div>
                    <div>
                        <span class="text-slate-500 block">Est. Salary (India)</span>
                        <span class="font-semibold text-slate-200">${role.salary_range?.in || '₹7 - ₹16 LPA'}</span>
                    </div>
                </div>
                <div class="mb-3">
                    <span class="text-xs text-slate-400 block mb-1.5">Matched Core Skills:</span>
                    <div class="flex flex-wrap gap-1.5">
                        ${(role.matched_skills || []).slice(0, 5).map(s => `<span class="px-2 py-0.5 rounded text-[11px] bg-emerald-950/60 border border-emerald-800/60 text-emerald-300">${s}</span>`).join('')}
                    </div>
                </div>
                ${role.missing_skills?.length ? `
                <div>
                    <span class="text-xs text-slate-400 block mb-1.5">Skills to Bridge:</span>
                    <div class="flex flex-wrap gap-1.5">
                        ${role.missing_skills.map(s => `<span class="px-2 py-0.5 rounded text-[11px] bg-rose-950/60 border border-rose-800/60 text-rose-300">+ ${s}</span>`).join('')}
                    </div>
                </div>` : ''}
            </div>
        `;
    });
}

// Module 3: Resume–Job Match Percentage
function renderResumeJobMatch(data) {
    const match = data.match_analysis || {};
    const score = match.overall_match_score || 72;

    document.getElementById('jobMatchScoreNumber').textContent = `${score}%`;
    document.getElementById('jobMatchVerdict').textContent = match.match_verdict || '';
    document.getElementById('hardSkillMatchPct').textContent = `${match.hard_skill_match_pct || 0}%`;
    document.getElementById('softSkillMatchPct').textContent = `${match.soft_skill_match_pct || 0}%`;
    document.getElementById('semanticSimPct').textContent = `${match.semantic_similarity_pct || 0}%`;

    // Progress bar fills
    document.getElementById('hardSkillProgressBar').style.width = `${match.hard_skill_match_pct || 0}%`;
    document.getElementById('softSkillProgressBar').style.width = `${match.soft_skill_match_pct || 0}%`;
    document.getElementById('semanticProgressBar').style.width = `${match.semantic_similarity_pct || 0}%`;

    // Matched skills tags
    const matchedContainer = document.getElementById('matchedSkillsTags');
    matchedContainer.innerHTML = '';
    (match.matched_skills || []).forEach(s => {
        matchedContainer.innerHTML += `<span class="px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-950/60 border border-emerald-700/60 text-emerald-300 flex items-center gap-1"><i data-lucide="check" class="w-3 h-3"></i>${s}</span>`;
    });

    // Missing skills tags
    const missingContainer = document.getElementById('missingSkillsPreviewTags');
    missingContainer.innerHTML = '';
    (match.missing_skills || []).forEach(s => {
        missingContainer.innerHTML += `<span class="px-2.5 py-1 rounded-full text-xs font-medium bg-rose-950/60 border border-rose-700/60 text-rose-300 flex items-center gap-1"><i data-lucide="alert-circle" class="w-3 h-3"></i>${s}</span>`;
    });
}

// Module 4: Skill Analysis
function renderSkillAnalysis(data) {
    const skillsData = data.skill_analysis || {};
    document.getElementById('totalSkillsCount').textContent = `${skillsData.total_skills_count || 0} Skills Detected`;

    const categoriesGrid = document.getElementById('skillCategoriesGrid');
    categoriesGrid.innerHTML = '';

    const categoryTitles = {
        languages: "Programming Languages",
        frameworks_libraries: "Frameworks & Libraries",
        databases: "Databases & Storage",
        cloud_devops: "Cloud & DevOps",
        developer_tools_architecture: "Developer Tools & Architecture",
        ai_data_science: "AI & Data Science",
        security_networking: "Security & Protocols",
        soft_skills: "Soft Skills & Methodologies"
    };

    const byCat = skillsData.by_category || {};

    Object.entries(byCat).forEach(([catKey, skillList]) => {
        if (!skillList || skillList.length === 0) return;
        const title = categoryTitles[catKey] || catKey.replace('_', ' ');

        categoriesGrid.innerHTML += `
            <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800">
                <div class="flex items-center justify-between mb-3">
                    <h5 class="text-sm font-semibold text-slate-200 capitalize">${title}</h5>
                    <span class="text-xs px-2 py-0.5 rounded-full bg-slate-800 text-indigo-400 font-mono">${skillList.length}</span>
                </div>
                <div class="flex flex-wrap gap-1.5">
                    ${skillList.map(s => `<span class="px-2.5 py-1 rounded-md text-xs bg-slate-800/90 text-slate-300 border border-slate-700">${s}</span>`).join('')}
                </div>
            </div>
        `;
    });
}

// Module 5: Missing Skills
function renderMissingSkills(data) {
    const missingSkills = data.missing_skills || [];
    const container = document.getElementById('missingSkillsDetailedContainer');
    container.innerHTML = '';

    if (missingSkills.length === 0) {
        container.innerHTML = '<div class="p-6 text-center text-slate-400">Awesome! No critical skill gaps detected for this role.</div>';
        return;
    }

    missingSkills.forEach(item => {
        const priorityColors = {
            "High Priority": "border-rose-700/60 bg-rose-950/20 text-rose-300",
            "Medium Priority": "border-amber-700/60 bg-amber-950/20 text-amber-300",
            "Nice to Have": "border-blue-700/60 bg-blue-950/20 text-blue-300"
        };

        const badgeClass = priorityColors[item.priority] || "border-slate-700 bg-slate-800 text-slate-300";

        container.innerHTML += `
            <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div class="space-y-1">
                    <div class="flex items-center gap-2">
                        <span class="text-base font-bold text-white">${item.skill}</span>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold border ${badgeClass}">${item.priority}</span>
                    </div>
                    <p class="text-xs text-slate-400">${item.why_needed}</p>
                </div>
                <div class="flex items-center gap-4 shrink-0 text-xs text-slate-300">
                    <div class="flex items-center gap-1.5">
                        <i data-lucide="clock" class="w-3.5 h-3.5 text-indigo-400"></i>
                        <span>${item.time_to_learn}</span>
                    </div>
                    <div class="flex items-center gap-1.5">
                        <i data-lucide="bar-chart-2" class="w-3.5 h-3.5 text-purple-400"></i>
                        <span>${item.difficulty}</span>
                    </div>
                </div>
            </div>
        `;
    });
}

// Module 6: Personalized Learning Roadmap
function renderPersonalizedRoadmap(data) {
    const roadmap = data.learning_roadmap || [];
    const container = document.getElementById('roadmapPhasesTimeline');
    container.innerHTML = '';

    roadmap.forEach((phase, idx) => {
        container.innerHTML += `
            <div class="relative pl-8 pb-8 border-l-2 border-indigo-500/40 last:border-transparent">
                <div class="absolute -left-2.5 top-0 w-5 h-5 rounded-full bg-indigo-600 border-4 border-slate-900"></div>
                <div class="glass-card p-5 rounded-xl border border-slate-800">
                    <div class="flex items-center justify-between flex-wrap gap-2 mb-2">
                        <h4 class="text-base font-bold text-white">${phase.phase}</h4>
                        <span class="px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-950 text-indigo-300 border border-indigo-800">${phase.duration}</span>
                    </div>
                    <p class="text-xs text-slate-400 mb-3 italic">Objective: ${phase.goal}</p>
                    <div class="space-y-2 mb-4">
                        ${phase.topics.map((t, tIdx) => `
                            <div class="flex items-center gap-2.5 text-xs text-slate-300">
                                <input type="checkbox" id="check_${idx}_${tIdx}" class="roadmap-checkbox rounded bg-slate-800 border-slate-700 text-indigo-600 focus:ring-indigo-500">
                                <label for="check_${idx}_${tIdx}" class="cursor-pointer select-none">${t}</label>
                            </div>
                        `).join('')}
                    </div>
                    <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-800/80">
                        ${phase.resources.map(r => `
                            <span class="text-[11px] px-2.5 py-1 rounded bg-slate-800/80 text-slate-300 border border-slate-700 flex items-center gap-1.5">
                                <i data-lucide="book-open" class="w-3 h-3 text-indigo-400"></i> ${r.name} (${r.type})
                            </span>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
    });
}

// Module 7: Recommended Projects
function renderRecommendedProjects(data) {
    const projects = data.recommended_projects || [];
    const container = document.getElementById('recommendedProjectsGrid');
    container.innerHTML = '';

    projects.forEach(proj => {
        container.innerHTML += `
            <div class="glass-card p-5 rounded-xl border border-slate-800 flex flex-col justify-between">
                <div>
                    <h4 class="text-lg font-bold text-white mb-2">${proj.title}</h4>
                    <p class="text-xs text-slate-300 mb-4">${proj.summary}</p>
                    <div class="mb-4">
                        <span class="text-xs text-slate-400 block mb-1.5">Tech Stack:</span>
                        <div class="flex flex-wrap gap-1.5">
                            ${proj.tech_stack.map(tech => `<span class="px-2 py-0.5 rounded text-xs bg-indigo-950/60 border border-indigo-800/60 text-indigo-300">${tech}</span>`).join('')}
                        </div>
                    </div>
                    <div class="mb-4">
                        <span class="text-xs text-slate-400 block mb-1.5">Core Features to Implement:</span>
                        <ul class="space-y-1 text-xs text-slate-300">
                            ${proj.key_features.map(f => `<li class="flex items-start gap-1.5"><i data-lucide="check-square" class="w-3.5 h-3.5 text-emerald-400 shrink-0 mt-0.5"></i>${f}</li>`).join('')}
                        </ul>
                    </div>
                </div>
                <div class="pt-3 border-t border-slate-800 mt-2">
                    <div class="flex items-center justify-between text-xs text-slate-400 mb-1">
                        <span>Ready-to-Use Resume Bullet:</span>
                        <button type="button" class="copy-btn text-indigo-400 hover:text-white" onclick="copyText('${proj.resume_bullet.replace(/'/g, "\\'")}')" title="Copy bullet">
                            <i data-lucide="copy" class="w-3.5 h-3.5"></i>
                        </button>
                    </div>
                    <p class="text-xs text-emerald-300 bg-slate-900/80 p-2.5 rounded border border-slate-800 italic">${proj.resume_bullet}</p>
                </div>
            </div>
        `;
    });
}

// Module 8: Interview Questions
function renderInterviewQuestions(data) {
    const questions = data.interview_questions || [];
    const container = document.getElementById('interviewQuestionsList');
    container.innerHTML = '';

    questions.forEach((q, idx) => {
        container.innerHTML += `
            <div class="p-4 rounded-xl bg-slate-900/60 border border-slate-800">
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-indigo-950 text-indigo-300 border border-indigo-800 uppercase tracking-wide">${q.category || 'Technical'}</span>
                    <button type="button" class="text-xs text-indigo-400 hover:underline" onclick="toggleAccordion('answer_${idx}')">Toggle Model Answer</button>
                </div>
                <h5 class="text-sm font-semibold text-white mb-2">${q.question}</h5>
                <div id="answer_${idx}" class="mt-3 pt-3 border-t border-slate-800/80 text-xs text-slate-300 space-y-2">
                    <div class="font-medium text-slate-400">Key Concepts to Highlight:</div>
                    <ul class="list-disc list-inside space-y-1 text-slate-300 pl-1">
                        ${(q.key_points || [q.what_interviewers_look_for || 'Key evaluation point']).map(pt => `<li>${pt}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
    });
}

// Helper: Toggle Accordion
function toggleAccordion(elementId) {
    const el = document.getElementById(elementId);
    if (el) {
        el.classList.toggle('hidden');
    }
}

// Helper: Tab Switching
function switchTab(tabId) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-content').forEach(c => c.classList.add('hidden'));

    const activeBtn = document.querySelector(`.tab-btn[data-tab="${tabId}"]`);
    const activeContent = document.getElementById(tabId);

    if (activeBtn) activeBtn.classList.add('active');
    if (activeContent) activeContent.classList.remove('hidden');

    // Refresh charts if switching to overview
    if (tabId === 'tabOverview' && radarChartInstance) {
        radarChartInstance.resize();
    }
}

// Helper: Copy Text to Clipboard
function copyText(text) {
    navigator.clipboard.writeText(text).then(() => {
        showToast('Copied to clipboard!', 'success');
    }).catch(err => {
        console.error('Clipboard copy failed:', err);
    });
}

// Helper: Export / Print Full Report
function exportReport() {
    if (!currentAnalysisData) {
        showToast('Please run an analysis first.', 'error');
        return;
    }
    // Open print view in new window
    fetch(`${API_BASE_URL}/api/export-report`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(currentAnalysisData)
    }).then(resp => resp.text())
      .then(html => {
          const printWindow = window.open('', '_blank');
          printWindow.document.write(html);
          printWindow.document.close();
      });
}

// Helper: Reset Everything
function resetAll() {
    uploadedFile = null;
    currentAnalysisData = null;
    selectedInterests.clear();
    removeSelectedFile();
    document.getElementById('resumeTextInput').value = '';
    document.getElementById('targetJdInput').value = '';
    document.getElementById('resultsSection').classList.add('hidden');
    document.getElementById('interestTagsContainer').querySelectorAll('button').forEach(btn => {
        btn.classList.remove('bg-indigo-600', 'text-white', 'border-indigo-500');
        btn.classList.add('bg-slate-800/80', 'text-slate-300', 'border-slate-700');
    });
    showToast('Reset form fields.');
}

// Helper: Show Toast Notifications
function showToast(msg, type = 'info') {
    const toast = document.getElementById('toastNotification');
    const toastMsg = document.getElementById('toastMessage');
    if (!toast || !toastMsg) return;

    toastMsg.textContent = msg;
    toast.classList.remove('hidden', 'translate-y-10', 'opacity-0');
    toast.classList.add('translate-y-0', 'opacity-100');

    setTimeout(() => {
        toast.classList.add('translate-y-10', 'opacity-0');
        setTimeout(() => toast.classList.add('hidden'), 300);
    }, 3200);
}

// Helper: Show/Hide Loading Overlay
function showLoading(show) {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) {
        if (show) overlay.classList.remove('hidden');
        else overlay.classList.add('hidden');
    }
}
