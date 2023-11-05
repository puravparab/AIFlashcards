import Image from 'next/image'
import FileUpload from "./components/file_upload.js"
import styles from './styles/page.module.css'

export default function Home() {
  return (
    <div className={styles.main}>
      <FileUpload />
    </div>
  )
}
