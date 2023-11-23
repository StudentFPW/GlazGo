export interface ITheme {
  colors: {
    primary: string
    inactive: string
    black: string
    white: string
    gray:  string
    lightGray: string
  }
  sizes: {
    container: { width: number }
  },
  order: {
    header: number
    burger: number
}
}