'use client'
import { useState, useEffect } from 'react'
import FlashCards from '../../components/flashcard.js'
import styles from '../../styles/page.module.css'

const Page = ({ params }) => {
  const [data, setData] = useState('')

  useEffect(() => {
    getData()
  }, [])
  const getData = async () => {
    const url = process.env.NEXT_PUBLIC_SERVER_URL + `/document/${params.id}`
    const res = await fetch(url, {
      method: 'GET'
    })

    if (res.ok){
      const responseData = await res.json()
      setData(responseData)
    } else{
      console.error("Document data invalld")
    }
  }

  return (
    <div className={styles.documentPage}>
      <div>
         <h2>Document #{params.id}</h2>
        {data != '' && <a href={data.file}>Link</a>}
      </div>

      {data != '' && 
        <FlashCards data={data} />
      }
    </div>
  )
}

export default Page