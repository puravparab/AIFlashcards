'use client'
import { useState } from 'react'

const Page = ({ params }) => {
  const [data, setData] = useState('')

  return (
    <div>
      My Post: {params.id}
    </div>
  )
}

export default Page