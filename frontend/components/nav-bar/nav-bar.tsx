'use client';
import Link from "next/link";
import classNames from "classnames";
import styles from "./nav-bar.module.css"
import type { NavBarProps } from "./interfaces";
import { useState } from "react";

export default function NavBar({ }: NavBarProps): JSX.Element {
  const [open, setOpen] = useState(false);
  return (
    <nav className={styles["nav-bar"]}>
      <Link href={"/"}>
        <h1 className="nav-title">SWAY RANKINGS</h1>
      </Link>
      <ul className={classNames(styles["nav-menu-items"], open && styles["open"])}>
        <li className={styles["list-item"]}> <Link href="/tournaments">Tournaments</Link></li>
        <li className={styles["list-item"]}> <Link href="/about">About</Link></li>
        <li className={styles["list-item"]}> <Link href="/about">Admin</Link></li>
      </ul>

      <button className={classNames(styles["nav-menu-dropdown"], open && styles["open"])} onClick={() => setOpen(!open)}>Icon</button>
    </nav>
  );
}
