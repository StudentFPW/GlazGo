import { css, styled } from "styled-components";

export const Container = styled.div`
  max-width: ${({ theme }) => theme.sizes.container.width + 30}px;
  padding: 0 15px;
  margin: 0 auto;
  width: 100%;
`
export const button = css`
    height: 46px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 8px;
    border: none;
`
export const FButton = styled.button`
    ${button}
    color: ${({ theme }) => theme.colors.white};
    background-color: ${({ theme }) => theme.colors.primary};
    &&[disabled] {
        background-color: ${({ theme }) => theme.colors.inactive};
    }
`
export const LButton = styled.button`
    ${button}
    background-color: ${({ theme }) => theme.colors.white};
    border: 0.5px solid ${({ theme }) => theme.colors.gray};
    box-shadow: 0px 4px 4px 0px rgba(17, 30, 62, 0.06)
`
export const NButton = styled(LButton)`
    width: 40px;
    height: 40px;
`
export const tButton = css`
    height: 40px;
    padding: 0 12px;
    width: auto;
    font-size: 14px;
    font-weight: 500;
    line-height: 18px; /* 128.571% */
    letter-spacing: -0.07px;
    column-gap: 4px;
`
export const TButton = styled(LButton)`
    ${tButton}
`
export const TFButton = styled(FButton)`
    ${tButton}
`
export const H2 = styled.h2`
    font-size: 26px;
    font-weight: 700;
    line-height: 32px; /* 123.077% */
    letter-spacing: -0.13px;
    margin: 24px 0;
`
export const input = css`
    height: 48px;
    padding: 12px 16px;
    border-radius: 8px;
    background: ${({ theme }) => theme.colors.lightGray};
    border: 1px solid ${({ theme }) => theme.colors.gray};
`
export const SvgIconWrapper = styled.div`
    height: 24px;
`