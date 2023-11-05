'use client'

import { useState, useEffect } from 'react';
import { redirect } from 'next/navigation'
import styles from '../styles/file_upload.module.css'

const FileUpload = () => {
	const [droppedFile, setDroppedFile] = useState(null)
	const [fileID, setFileID] = useState(null)
	const [step, setStep] = useState(1)

	useEffect(() => {
		if (step == 2){
			// chat()
			redirect(`/document/${fileID}`)
		}
	}, [step])

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
		if (droppedFile){
			let url = process.env.NEXT_PUBLIC_SERVER_URL + "upload/"
			const formData = new FormData();
			formData.append('file', droppedFile);

			const res = await fetch(url, {
				method: 'POST',
				body: formData,
			})
			if (res.ok){
				let responseData = await res.json();
				setFileID(responseData.file_id)
				// Create and store embeddings
				url = process.env.NEXT_PUBLIC_SERVER_URL + "upload/" + responseData.file_id
				const response = await fetch(url, {
					method: 'POST',
					body: formData,
				})
				if (response.ok){
					responseData = await response.json();
					console.log(responseData)
					setStep(2)
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

// 	const chat = async () => {
// 		if (droppedFile){
// 			let url = process.env.NEXT_PUBLIC_SERVER_URL + "upload/chat"
// 
// 			const formData = new FormData()
// 			formData.append('file', droppedFile)
// 			const res = await fetch(url, {
// 				method: "POST",
// 				body: formData
// 			})
// 			if (res.ok){
// 				const responseData = await res.json()
// 				console.log(responseData)
// 			} else {
// 				console.error("Chat completion failed")
// 			}
// 		}
// 	}

	return (
		<div className={styles.fileUploadContainer}>
			{step == 1 && 
				<>
					<div 
						className={styles.fileUploadBox}
						onDrop={handleFileDrop}
						onDragOver={handleDragOver}
					>
						<span>Drag and drop file here</span>
					</div>
					<button onClick={handleSubmit}>
						<span>Create!</span>
					</button>
				</>
			}
			{step == 2 &&
				<div>
				</div>
			}
		</div>
	)
}

export default FileUpload