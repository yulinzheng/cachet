import React, { useState, useEffect } from 'react'

const NotesListPage = () => {
    let [notes, setNotes] = useState([])

    useEffect(() => {
        fetch('http://localhost:8000/api/notes/')
            .then(response => response.json())
            .then(data => setNotes(data.results))
            .catch(error => console.error('Error fetching notes:', error));
    }, []);

    return (
        <div>
            <h1>Notes</h1>
            <ul>
                {notes.map((note, index) => (
                    <li key={index}>
                        <div>
                            <h3>{note.title}</h3>
                            <p>{note.body}</p>
                            <p>Created At: {note.created_at}</p>
                            <p>Updated At: {note.updated_at}</p>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default NotesListPage
