import React from 'react';

export default function UserBio({ rawHtmlBio }) {
    // Semgrep flags this: dangerouslySetInnerHTML used with an un-sanitized prop
    return (
        <div className="bio-container" 
             dangerouslySetInnerHTML={{ __html: rawHtmlBio }} />
    );
}