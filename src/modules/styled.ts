export interface ITheme {
  colors: {
    primary: string,
    inactive: string
  }
  sizes: {
    container: { width: number }
  },
  order: {
    header: number
    headerAbove: number
}
}