import { Inter } from '@next/font/google'
import styles from './page.module.css'
import { Player } from '@/lib/types_be'

const inter = Inter({ subsets: ['latin'] })

export default async function Home() {
  const data = await getData()
  return (
    <main className={styles.main}>
      <div className={styles.description}>
        <p>
          Get Players
        </p>
        <ol>
          {data.map((d: Player, index: number) => {
            return <li key={index}>{d.gamer_tag}</li>
          })}
        </ol>
      </div>
    </main>
  )
}

export async function getData() {
  const response = await fetch("http://127.0.0.1:8000/api/players")

  return response.json()
}