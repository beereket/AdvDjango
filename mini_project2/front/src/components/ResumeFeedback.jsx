import React, { useState, useEffect } from 'react';

const ResumeFeedback = ({ resumeData }) => {
    const [feedback, setFeedback] = useState(null);

    useEffect(() => {
        if (resumeData) {
            // Имитация запроса к API
            setFeedback({
                skills: 'Missing key skills for job',
                formatting: 'Poor formatting',
                keywords: 'Needs more job-related keywords',
            });
        }
    }, [resumeData]);

    return (
        <div className="container mx-auto p-6">
            {feedback ? (
                <div>
                    <h3 className="text-xl">Feedback:</h3>
                    <ul>
                        {feedback.skills && <li>Skills Gaps: {feedback.skills}</li>}
                        {feedback.formatting && <li>Formatting Issues: {feedback.formatting}</li>}
                        {feedback.keywords && <li>Keyword Optimization: {feedback.keywords}</li>}
                    </ul>
                </div>
            ) : (
                <p>No feedback available yet.</p>
            )}
        </div>
    );
};

export default ResumeFeedback;
