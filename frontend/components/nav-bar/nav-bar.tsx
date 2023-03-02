import Link from "next/link";
import type { NavBarProps } from "./interfaces";

export default function NavBar({ }: NavBarProps): JSX.Element {
  return (
    <nav className="nav-bar">
      <Link href={"/"}>
        <h1>SWAY GGST RANKINGS</h1>
      </Link>
      <div className="nav-menu-item">
        <ul>
          <li> <Link href="/tournaments">Tournaments</Link></li>
          <li> <Link href="/about">About</Link></li>
          <li> <Link href="/about">Admin</Link></li>
        </ul>
      </div>
    </nav>
  );
}
