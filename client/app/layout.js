import './globals.css'

// import Footer from './components/footer/footer.js'
// import { VercelAnalytics } from './components/analytics/va.js';
// import { GTag } from './components/analytics/gtag.js';

import { Inter } from 'next/font/google'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Flashcard.ai',
  description: 'AI generated flashcards',
  other: {
  }
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      {/* <GTag /> */}
      <body className={inter.className}>
        {children}
        {/* <Footer /> */}
        {/* <VercelAnalytics /> */}
      </body>
    </html>
  )
}
