'use client'

import { useState } from 'react';
import styles from '../styles/file_upload.module.css'

const FileUpload = () => {
	const [droppedFile, setDroppedFile] = useState(null)

	const handleFileDrop = (e) => {
		e.preventDefault()
		const file = event.dataTransfer.files[0];
		
		if (file) {
			setDroppedFile(file);
			console.log(file)
		}
	}

	const handleDragOver = (e) => {
		e.preventDefault()
	}

	const handleSubmit = (e) => {
		e.preventDefault()
	}

	return (
		<>
			<p>Drop files here</p>
			<div 
				className={styles.fileUploadBox}
				onDrop={handleFileDrop}
				onDragOver={handleDragOver}
			>
			</div>
			<button onClick={handleSubmit}>
				Create!
			</button>
		</>
		
	)
}

export default FileUpload