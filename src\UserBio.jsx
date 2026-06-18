import React from 'react';
import DOMPurify from 'dompurify';

/**
 * UserBio component displays a user's biography, sanitizing any HTML content
 * to prevent Cross-Site Scripting (XSS) vulnerabilities.
 * 
 * @param {object} props - The component props.
 * @param {string} props.bio - The user's biography content, potentially containing HTML.
 */
function UserBio({ bio }) {
  // Ensure bio is treated as a string for sanitization
  const bioString = String(bio || '');
  
  // Sanitize the bio content using DOMPurify before setting it as inner HTML.
  // This removes any potentially malicious scripts or tags, preventing XSS attacks.
  const sanitizedBio = DOMPurify.sanitize(bioString);

  return (
    <div dangerouslySetInnerHTML={{ __html: sanitizedBio }} />
  );
}

export default UserBio;
