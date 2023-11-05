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
		}
	}

	const handleDragOver = (e) => {
		e.preventDefault()
	}

	const handleSubmit = async () => {
		console.log(droppedFile)
		if (droppedFile){
			let url = process.env.NEXT_PUBLIC_SERVER_URL + "upload/"
			console.log(url)
			// Create a FormData object and append the file to it
			const formData = new FormData();
			formData.append('file', droppedFile);

			// Replace 'your_api_endpoint' with the actual API endpoint where you want to submit the file
			const res = await fetch(url, {
				method: 'POST',
				body: formData,
			})
			if (res.ok){
				let responseData = await res.json();
				url = process.env.NEXT_PUBLIC_SERVER_URL + "upload/" + responseData.file_id
				const response = await fetch(url, {
					method: 'POST',
					body: formData,
				})
				if (response.ok){
					responseData = await response.json();
					console.log('File submitted successfully!')
					
				}
				else{
					console.error('File submission failed.');
				}
			}
			else{
				console.error('File submission failed.');
			}
		}
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