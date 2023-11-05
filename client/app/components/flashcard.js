import {useState} from 'react'

const FlashCards = (props) => {
	console.log(props.data)
	const [index, setIndex] = useState(0)
	const [revealAns, setRevealAns] = useState(false)

	return (
		<div>
			{/* {revealAns */}
			{/* ? <p>{props.data[index]["Q"]}</p> */}
			{/* : <p>{props.data[index]["A"]}</p> */}
			{/* } */}
		</div>
	)
}

export default FlashCards