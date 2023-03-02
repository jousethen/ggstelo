import Link from "next/link";
import styles from "./nav-bar.module.css"
import type { NavBarProps } from "./interfaces";

export default function NavBar({ }: NavBarProps): JSX.Element {
  return (
    <nav className={styles["nav-bar"]}>
      <Link href={"/"}>
        <h1 className="nav-title">SWAY RANKINGS</h1>
      </Link>
      <ul className={styles["nav-menu-items"]}>
        <li> <Link href="/tournaments">Tournaments</Link></li>
        <li> <Link href="/about">About</Link></li>
        <li> <Link href="/about">Admin</Link></li>
      </ul>

      <button className={styles["nav-menu-dropdown"]}>Icon</button>
    </nav>
  );
}
